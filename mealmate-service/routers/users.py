from fastapi import (
    APIRouter,
    Response,
    Depends,
    status,
    Request,
    HTTPException,
)
from jwtdown_fastapi.authentication import Token
from authenticator import authenticator
from pydantic import BaseModel
from queries.users import UserIn, UserOut, UserQueries, UserOutWithPassword
from typing import List


class DuplicateAccountError(ValueError):
    pass


class AccountForm(BaseModel):
    username: str
    password: str


class AccountToken(Token):
    account: UserOut


class HttpError(BaseModel):
    message: str


router = APIRouter()


# ####USER SIGNUP#####
@router.post("/users/", response_model=AccountToken | HttpError)
async def create_user(
    info: UserIn,
    request: Request,
    response: Response,
    repo: UserQueries = Depends(),
):
    hashed_password = authenticator.hash_password(info.password)
    try:
        account = repo.create(info, hashed_password)
    except DuplicateAccountError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot create user",
        )
    form = AccountForm(username=info.username, password=info.password)
    print(account)
    token = await authenticator.login(response, request, form, repo)
    return AccountToken(account=account, **token.dict())


# ####TOKEN#####
@router.get("/token/", response_model=AccountToken | None)
async def get_token(
    request: Request,
    account: UserIn = Depends(authenticator.try_get_current_account_data),
) -> AccountToken | None:
    if account and authenticator.cookie_name in request.cookies:
        return {
            "access_token": request.cookies[authenticator.cookie_name],
            "type": "Bearer",
            "account": account,
        }


# ####GET USER#####
@router.get("/users/{user_id}/", response_model=UserOutWithPassword)
def get_one_user(
    user_id: int,
    repo: UserQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
) -> UserOutWithPassword:
    try:
        return repo.get_user(user_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot get user",
        )


# ####UPDATE USER#####
@router.put("/users/{user_id}/", response_model=UserOut)
def update_user(
    user_id: int,
    user: UserIn,
    repo: UserQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
) -> UserOut:
    try:
        return repo.update_user(user_id, user)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot update user",
        )


# ####DELETE USER#####
@router.delete("/users/{user_id}/", response_model=bool)
def delete_user(
    user_id: int,
    repo: UserQueries = Depends(),
    account_data: dict = Depends(authenticator.get_current_account_data),
) -> bool:
    try:
        return repo.delete_user(user_id)
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot delete user",
        )


# ####GET ALL USERS#####
@router.get("/users/", response_model=List[UserOutWithPassword])
def get_all_users(
    resp: Response,
    repo: UserQueries = Depends(),
    # account_data: dict = Depends(authenticator.get_current_account_data),
):
    try:
        result = repo.get_all_users()
        if result is None:
            resp.status_code = 500
        return result
    except ValueError:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Cannot get all users",
        )
