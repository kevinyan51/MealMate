from pydantic import BaseModel
from typing import Optional
from queries.pool import pool


class Error(BaseModel):
    message: str

class MealOut(BaseModel):
    id: int
    name: str
    picture_url: str
    description: str
    instructions: str
    ingredients: str
    chef_id: int


class MealDetailsRepository:
    def get_one(self, meals_id: int) -> Optional[MealOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    result = cur.execute(
                        """
                        SELECT id
                            , name
                            , picture_url
                            , description
                            , instructions
                            , ingredients
                            , chef_id
                        FROM meals
                        WHERE id = %s
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
            name=record[1],
            picture_url=record[2],
            description=record[3],
            instructions=record[4],
            ingredients=record[5],
            chef_id=record[6],
        )
