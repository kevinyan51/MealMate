from fastapi import APIRouter, Depends, Response
from typing import List, Optional, Union
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
