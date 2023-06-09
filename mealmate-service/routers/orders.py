from fastapi import APIRouter, Depends, Response
from typing import List, Union
from queries.orders import Error, OrderOut, OrderRepo

router = APIRouter()


@router.get(
    "/users/{user_id}/orders", response_model=Union[List[OrderOut], Error]
)
def get_orders_by_subscriber(
    user_id: int,
    resp: Response,
    repo: OrderRepo = Depends(),
):
    result = repo.get_all_by_user(user_id)
    if result is None:
        resp.status_code = 500
    return result


@router.get("/orders", response_model=Union[List[OrderOut], Error])
def get_all_orders(
    resp: Response,
    repo: OrderRepo = Depends(),
):
    result = repo.get_all()
    if result is None:
        resp.status_code = 500
    return result


@router.post("/orders", response_model=Union[OrderOut, Error])
def create_order(
    box_id: int,
    resp: Response,
    repo: OrderRepo = Depends(),
):
    print("-=========================")
    print("box_id", box_id)
    print("-=========================")
    result = repo.create(box_id)
    if result is None:
        resp.status_code = 500
    return result


@router.get("/orders/{order_id}", response_model=Union[OrderOut, Error])
def get_one_order(
    order_id: int,
    resp: Response,
    repo: OrderRepo = Depends(),
):
    result = repo.get_one(order_id)
    if result is None:
        resp.status_code = 500
    return result


@router.get(
    "/users/{user_id}/orders/meals/{meal_id}",
    response_model=Union[bool, Error],
)
def check_if_subscriber_ordered_meal(
    subscriber_id: int,
    meal_id: int,
    resp: Response,
    repo: OrderRepo = Depends(),
):
    result = repo.if_ordered_meal(subscriber_id, meal_id)
    if result is None:
        resp.status_code = 500
    return result
