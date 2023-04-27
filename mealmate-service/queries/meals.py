from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import datetime
from queries.pool import pool


class Error(BaseModel):
    message: str


class MealOut(BaseModel):
    meal_id: Optional[int]
    status_id: Optional[int]
    chef_id: Optional[int]
    name: Optional[str]
    name2: Optional[str]
    created_at: Optional[datetime]
    updated_at: Optional[datetime]
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
    price: Union[Optional[float], Optional[int]]
    chef_first_name: Optional[str]
    chef_last_name: Optional[str]
    chef_picture_url: Optional[str]


class MealRepo:
    def get_all(self) -> Union[List[MealOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT m.*, u.first_name, u.last_name, u.picture_url
                        FROM meals m
                        JOIN users u on m.chef_id = u.id
                        WHERE m.status_id = 6;
                        """
                    )
                    recs = cur.fetchall()
                    return [self.record_to_mealout(rec) for rec in recs]
        except Exception as e:
            # print(f"******\nError Message:\n\n {e}\n******")
            return Error(message=str(e))

    def get_all_by_user(self, user_id: int) -> Union[List[MealOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT m.*, u.first_name, u.last_name, u.picture_url
                        FROM meals m
                        JOIN users u on m.chef_id = u.id
                        WHERE m.chef_id = %s
                        AND m.status_id = 6;
                        """,
                        [user_id],
                    )
                    recs = cur.fetchall()
                    return [self.record_to_mealout(rec) for rec in recs]
        except Exception as e:
            # print(f"******\nError Message:\n\n {e}\n******")
            return Error(message=str(e))

    def record_to_mealout(self, record):
        return MealOut(
            meal_id=record[0],
            status_id=record[1],
            chef_id=record[2],
            name=record[3],
            name2=record[4],
            created_at=record[5],
            updated_at=record[6],
            picture_url=record[7],
            description=record[8],
            instructions=record[9],
            ingredients=record[10],
            calories=record[11],
            is_keto=record[12],
            is_vegan=record[13],
            is_chef_choice=record[14],
            is_spicy=record[15],
            has_cheese=record[16],
            price=record[17],
            chef_first_name=record[18],
            chef_last_name=record[19],
            chef_picture_url=record[20],
        )
