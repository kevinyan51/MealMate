from fastapi import APIRouter, Depends, Response
from typing import List, Optional, Union
from queries.meals import Error, MealOut, MealRepo


router = APIRouter()


@router.get("/meals/", response_model=Union[List[MealOut], Error])
def get_all(
    repo: MealRepo = Depends(),
):
    return repo.get_all()
