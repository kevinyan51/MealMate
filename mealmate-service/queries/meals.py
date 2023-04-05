from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import date
from queries.pool import pool


class Error(BaseModel):
    message: str


class MealOut(BaseModel):
    meal_id: Optional[int]
    chef_id: Optional[int]
    name: Optional[str]
    name2: Optional[str]
    created_at: Optional[date]
    updated_at: Optional[date]
    picture_url: Optional[str]
    description: Optional[str]
    instructions: Optional[str]
    ingredients: Optional[str]
    calories: Optional[int]
    is_keto: Optional[bool]
    is_vegan: Optional[bool]
    is_chef_choice: Optional[bool]
    is_spicy: Optional[bool]
    has_cheese: Optional[bool]
    chef_first_name: Optional[str]
    chef_last_name: Optional[str]
    price: Union[Optional[float], Optional[int]]


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

    def get_all_by_user(self, user_id: int) -> Union[List[MealOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT m.*, u.first_name, u.last_name
                        FROM meals m
                        JOIN users u on m.chef_id = u.id
                        WHERE m.chef_id = %s
                        """,
                        [user_id],
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
            meal_id=record[0],
            chef_id=record[1],
            name=record[2],
            name2=record[3],
            created_at=record[4],
            updated_at=record[5],
            picture_url=record[6],
            description=record[7],
            instructions=record[8],
            ingredients=record[9],
            calories=record[10],
            is_keto=record[11],
            is_vegan=record[12],
            is_chef_choice=record[13],
            is_spicy=record[14],
            has_cheese=record[15],
            chef_first_name=record[16],
            chef_last_name=record[17],
        )
