from fastapi import APIRouter, Depends, Response
from typing import List, Union
from queries.meals import Error, MealOut, MealRepo


router = APIRouter()


# @router.get("/meals/", response_model=Union[List[MealOut], Error])
# def get_all(
#     repo: MealRepo = Depends(),
# ):
#     return repo.get_all()


@router.get("/meals", response_model=Union[List[MealOut], Error])
def get_all_meals(
    resp: Response,
    repo: MealRepo = Depends(),
):
    result = repo.get_all()
    # if hasattr(result, "message"):
    if result is None:
        resp.status_code = 500
    return result


@router.get(
    "/users/{user_id}/meals", response_model=Union[List[MealOut], Error]
)
def get_meals_by_chef(
    user_id: int,
    resp: Response,
    repo: MealRepo = Depends(),
):
    result = repo.get_all_by_user(user_id)
    if result is None:
        resp.status_code = 500
    return result
