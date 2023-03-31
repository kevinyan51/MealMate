from fastapi import APIRouter, Depends, Response
from typing import Optional
from queries.meal_details import MealDetailsRepository, MealOut

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
