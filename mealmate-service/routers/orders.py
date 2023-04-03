from fastapi import APIRouter, Depends, Response
from typing import List, Optional, Union
from queries.orders import Error, OrderOut, OrderRepo

router = APIRouter()


@router.get("/orders/{order_id}/", response_model=Union[List[OrderOut], Error])
def get_orders_by_subscriber(
    order_id: int,
    resp: Response,
    repo: OrderRepo = Depends(),
):
    result = repo.get_one(order_id)
    if result is None:
        resp.status_code = 500
    return result


# def get_one_order(
#     order_id: int,
#     resp: Response,
#     repo: OrderRepo = Depends(),
# ):
#     result = repo.get_one(order_id)
#     if result is None:
#         resp.status_code = 500
#     return result
