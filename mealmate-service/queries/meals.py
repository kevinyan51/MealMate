from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import date
from queries.pool import pool


class Error(BaseModel):
    message: str


class MealOut(BaseModel):
    id: Optional[int]
    name: Optional[str]
    created_at: Optional[date]
    updated_at: Optional[date]
    picture_url: Optional[str]
    description: Optional[str]
    instructions: Optional[str]
    ingredients: Optional[str]
    chef_id: Optional[int]


class MealRepo:
    def get_all(self) -> Union[List[MealOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT *
                        FROM meals m
                        JOIN users u on m.chef_id = u.id
                        ORDER by m.created_at
                        """
                    )
                    print(cur.fetchone())
        except Exception as e:
            print("Error", e)
