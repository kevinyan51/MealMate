from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import date
from queries.pool import pool
from queries.boxes import MealOutWQty


class OrderOut(BaseModel):
    order_id: int
    subscriber_id: int
    subscriber_first_name: str
    subscriber_last_name: str
    order_date: date
    num_meals: int
    total_price: float
    meals: List[MealOutWQty]


class OrderRepo:
    pass
