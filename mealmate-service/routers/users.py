from authenticator import authenticator
from jwtdown_fastapi.authentication import Token
from pydantic import BaseModel
from fastapi import APIRouter, Response, Depends, status, Request, HTTPException
from queries.users import DuplicationAccountError, UserIn, UserOut, UserRepository


class AccountForm(BaseModel):
    username: str
    password: str


class AccountToken(Token):
    account: UserOut


class HttpError(BaseModel):
    message: str


router = APIRouter()


@router.get("/protected", response_model=bool, tags=["Users"])
async def protected(
    account_data: dict = Depends(authenticator.get_current_account_data),
):
    return True


@router.get("/users/all", tags=["Users"])
def get_all_users(
    repo: UserRepository = Depends(),
):
    return repo.get_all()


@router.get("/get/{username}", tags=["Users"])
def get_user(
    username: str,
    repo: UserRepository = Depends(),
) -> UserOut:
    return repo.get(username)


@router.post("/signup", tags=["Users"])
async def create_account(
    userdata: UserIn,
    request: Request,
    response: Response,
    repo: UserRepository = Depends(),
):
    hashed_password = authenticator.hash_password(userdata.password)
    print(hashed_password)
    print(userdata)
    try:
        account = repo.create(userdata, hashed_password)
    except DuplicationAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create account",
        )
    form = AccountForm(username=userdata.username, password=userdata.password)
    token = await authenticator.login(response, request, form, repo)
    return AccountToken(account=account, **token.dict())


@router.put("/update/{user_id}", tags=["users"])
def update_user(
    user_id: int,
    user: UserIn,
    repo: UserRepository = Depends(),
) -> UserOut:
    return repo.update(user_id, user)


@router.delete("/delete/{user_id}", tags=["users"])
def delete_user(
    user_id: int,
    repo: UserRepository = Depends(),
):
    return repo.delete(user_id)


@router.get("/token", response_model=AccountToken | None, tags=["users"])
async def get_token(
    request: Request,
    account: UserOut = Depends(authenticator.try_get_current_account_data),
) -> AccountToken | None:
    if account and authenticator.cookie_name in request.cookies:

        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "token_type": "Bearer",
            "account": account,
        }
