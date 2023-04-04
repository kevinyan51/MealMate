from fastapi import APIRouter, Depends, Response
from typing import Optional
from queries.meal_details import MealDetailsRepository, MealOut, ChefMealDetailsRepository

router = APIRouter()

@router.get("/meals/{meals_id}/",response_model = Optional[MealOut])
def get_one_meal(
    meals_id: int,
    response: Response,
    repo: MealDetailsRepository = Depends(),
) -> MealOut:
    meal = repo.get_one(meals_id)
    if meal is None:
        response.status_code = 404
    return meal


@router.get("users/{chef_id}/meals/{meals_id}/", response_model= Optional[MealOut])
def get_one_meal_chef(
    meals_id: int,
    chef_id: int,
    response: Response,
    repo: ChefMealDetailsRepository = Depends(),
) -> MealOut:
    meal = repo.get_one_meal_chef(meals_id, chef_id)
    if meal is None:
        response.status_code = 404
    return meal
