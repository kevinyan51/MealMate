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
    chef_first_name: Optional[str]
    chef_last_name: Optional[str]


class MealRepo:
    def get_all(self) -> Union[List[MealOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT m.*, u.first_name, u.last_name
                        FROM meals m
                        JOIN users u on m.chef_id = u.id;
                        """
                    )
                    recs = cur.fetchall()
                    return [self.record_to_mealout(rec) for rec in recs]
        except Exception as e:
            print(
                f"*********************************\nError Message:\n\n {e}\n*********************************"
            )
            return Error(message=str(e))

    def record_to_mealout(self, record):
        return MealOut(
            id=record[0],
            name=record[1],
            created_at=record[2],
            updated_at=record[3],
            picture_url=record[4],
            description=record[5],
            instructions=record[6],
            ingredients=record[7],
            chef_id=record[8],
            chef_first_name=record[9],
            chef_last_name=record[10],
        )
