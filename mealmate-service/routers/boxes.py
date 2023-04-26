from fastapi import APIRouter, Depends, Response
from typing import Union
from queries.boxes import Error, BoxInOut, BoxRepo


router = APIRouter()


@router.get("/users/{user_id}/box_id", response_model=Union[int, Error])
def get_user_box_id(
    user_id: int,
    resp: Response,
    repo: BoxRepo = Depends(),
):
    result = repo.get_user_box_id(user_id)
    if result is None:
        resp.status_code = 500
    return result


@router.get("/boxes/{box_id}", response_model=Union[BoxInOut, Error])
def get_one_box(
    box_id: int,
    resp: Response,
    repo: BoxRepo = Depends(),
):
    result = repo.get_one(box_id)
    if result is None:
        resp.status_code = 500
    return result


@router.put("/boxes/{box_id}", response_model=Union[BoxInOut, Error])
def update_box(
    box_id: int,
    box: BoxInOut,
    resp: Response,
    repo: BoxRepo = Depends(),
):
    result = repo.update(box_id, box)
    if result is None:
        resp.status_code = 500
    return result
