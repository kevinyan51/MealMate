from fastapi import APIRouter, Depends, Response
from typing import List, Union
from queries.reviews import Error, ReviewIn, ReviewOut, ReviewRepo

router = APIRouter()


@router.get("/reviews/", response_model=Union[List[ReviewOut], Error])
def get_all_reviews(
    resp: Response,
    repo: ReviewRepo = Depends(),
):
    result = repo.get_all()
    if result is None:
        resp.status_code = 500
    return result


@router.post("/reviews/", response_model=Union[ReviewOut, Error])
def create_review(
    review: ReviewIn,
    resp: Response,
    repo: ReviewRepo = Depends(),
):
    result = repo.create(review)
    if result is None:
        resp.status_code = 500
    return result


@router.get(
    "/users/{user_id}/reviews/", response_model=Union[List[ReviewOut], Error]
)
def get_reviews_by_subscriber(
    review_id: int,
    resp: Response,
    repo: ReviewRepo = Depends(),
):
    result = repo.get_all_by_user(review_id)
    if result is None:
        resp.status_code = 500
    return result


@router.get(
    "/meals/{meal_id}/reviews/", response_model=Union[List[ReviewOut], Error]
)
def get_reviews_by_meal(
    meal_id: int,
    resp: Response,
    repo: ReviewRepo = Depends(),
):
    result = repo.get_all_by_meal(meal_id)
    if result is None:
        resp.status_code = 500
    return result


@router.get("/reviews/{review_id}/", response_model=Union[ReviewOut, Error])
def get_one_review(
    review_id: int,
    resp: Response,
    repo: ReviewRepo = Depends(),
):
    result = repo.get_one(review_id)
    if result is None:
        resp.status_code = 500
    return result


@router.put("/reviews/{review_id}/", response_model=Union[ReviewOut, Error])
def update_review(
    review_id: int,
    review: ReviewIn,
    resp: Response,
    repo: ReviewRepo = Depends(),
):
    result = repo.update(review_id, review)
    if result is None:
        resp.status_code = 500
    return result


@router.delete("/reviews/{review_id}/", response_model=Union[ReviewOut, Error])
def delete_review(
    review_id: int,
    resp: Response,
    repo: ReviewRepo = Depends(),
):
    result = repo.delete(review_id)
    if result is None:
        resp.status_code = 500
    return result
