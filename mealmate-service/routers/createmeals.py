from fastapi import APIRouter, Depends, Response
from queries.createmeals import MealIn, MealOut, MealRepository, Error
from typing import Union


router = APIRouter()


@router.post("/meals/", response_model=Union[MealOut, Error])
def create_meal(
    meals: MealIn, response: Response, repo: MealRepository = Depends()
):
    result = repo.create(meals)
    if result is None:
        response.status_code = 500
    return result


@router.put("/meals/{meal_id}/", response_model=Union[MealOut, Error])
def update_meal(
    meal_id: int,
    meal: MealIn,
    repo: MealRepository = Depends(),
) -> Union[Error, MealOut]:
    return repo.update_meal(meal_id, meal)


@router.delete("/meals/{meal_id}/", response_model=bool)
def delete_meal(
    meal_id: int,
    repo: MealRepository = Depends(),
) -> bool:
    return repo.delete(meal_id)
