from fastapi import APIRouter, Depends, Response
from queries.createmeals import MealIn, MealOut, MealRepository, Error
from typing import Union


router = APIRouter()

@router.post("/meals/", response_model=Union[MealOut, Error])
def create_meal(meals: MealIn, response: Response, repo: MealRepository = Depends()):
    result = repo.create(meals)
    if result == None:
        response.status_code = 500
    return result
