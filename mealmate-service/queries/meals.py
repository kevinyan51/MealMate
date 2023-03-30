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
    def get_all(self) -> Union[Error, List[MealOut]]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    result = cur.execute(
                        """
                        SELECT id
                          , name
                          , created_at
                          , updated_at
                          , picture_url
                          , description
                          , instructions
                          , ingredients
                          , chef_id
                        FROM meals
                        ORDER BY created_at;
                        """
                    )
                    print("records")
                    print(result)

                    return [self.record_to_meal(record) for record in result]
        except Exception as e:
            print(e)
            return {"message": "Could not get all meals"}

    def record_to_meal(self, record):
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
        )
