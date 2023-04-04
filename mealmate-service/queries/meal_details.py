from pydantic import BaseModel
from typing import Optional
from queries.pool import pool
from datetime import date


class Error(BaseModel):
    message: str

class MealOut(BaseModel):
    id: int
    chef_id: int
    name: str
    name2: str
    created_at: date
    updated_at: date
    picture_url: str
    description: str
    instructions: str
    ingredients: str
    calories: int
    is_keto: bool
    is_vegan: bool
    is_chef_choice: bool
    is_spicy: bool
    has_cheese: bool
    price: float
    first_name: str
    last_name: str


class MealDetailsRepository:
    def get_one(self, meals_id: int) -> Optional[MealOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    result = cur.execute(
                        """
                        SELECT meals.id
                            , chef_id
                            , meals.name
                            , name2
                            , meals.created_at
                            , meals.updated_at
                            , meals.picture_url
                            , description
                            , instructions
                            , ingredients
                            , calories
                            , is_keto
                            , is_vegan
                            , is_chef_choice
                            , is_spicy
                            , has_cheese
                            , price
                            , first_name
                            , last_name
                        FROM meals
                        LEFT JOIN users
                        ON meals.chef_id = users.id
                        WHERE meals.id = %s
                        """,
                        [meals_id]
                    )
                    record = result.fetchone()
                    print("record *************",record)
                    if record is None:
                        return None
                    return self.record_to_meal_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not get meal details"}

    def record_to_meal_out(self, record):
        return MealOut(
            id=record[0],
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
            price=record[16],
            first_name=record[17],
            last_name=record[18]
        )






class ChefMealDetailsRepository:
    def get_one_meal_chef(self, meals_id: int, chef_id: int) -> Optional[MealOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    result = cur.execute(
                        """
                        SELECT meals.id
                            , chef_id
                            , meals.name
                            , name2
                            , meals.created_at
                            , meals.updated_at
                            , meals.picture_url
                            , description
                            , instructions
                            , ingredients
                            , calories
                            , is_keto
                            , is_vegan
                            , is_chef_choice
                            , is_spicy
                            , has_cheese
                            , price
                        FROM meals
                        LEFT JOIN users
                        ON meals.chef_id = users.id
                        WHERE meals.id = %s AND meals.chef_id = %s
                        """,
                        [meals_id, chef_id]
                    )
                    record = result.fetchone()
                    print("record *************",record)
                    if record is None:
                        return None
                    return self.chef_record_to_meal_out(record)
        except Exception as e:
            print(e)
            return {"message": "Could not get meal details"}

    def chef_record_to_meal_out(self, record):
        return MealOut(
            id=record[0],
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
            price=record[16],
        )
