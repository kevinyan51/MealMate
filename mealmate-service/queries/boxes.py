from typing import List, Union
from pydantic import BaseModel
from queries.pool import pool
from queries.meals import MealOut, Error


class MealOutWQty(MealOut):
    quantity: int


class BoxInOut(BaseModel):
    box_id: int
    subscriber_id: int
    subscriber_first_name: str
    subscriber_last_name: str
    meals: List[MealOutWQty]


class BoxRepo:
    def get_user_box_id(self, user_id: int) -> Union[int, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT id
                        FROM boxes
                        WHERE subscriber_id = %s
                        """,
                        [user_id],
                    )
                    rec = cur.fetchone()
                    return rec[0]
        except Exception as e:
            print(
                f"*********************************\nError Message:\n\n {e}\n*********************************"
            )
            return Error(message=str(e))

    def update(self, box_id: int, box: BoxInOut) -> Union[BoxInOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        DELETE FROM box_meals
                        WHERE box_id = %s
                        """,
                        [box_id],
                    )
                    for meal in box.meals:
                        cur.execute(
                            """
                            INSERT INTO box_meals (quantity, box_id, meal_id)
                            VALUES (%s, %s, %s)
                            """,
                            [meal.quantity, box_id, meal.meal_id],
                        )
                    return self.get_one(box_id)
        except Exception as e:
            print(
                f"*********************************\nError Message:\n\n {e}\n*********************************"
            )
            return Error(message=str(e))

    def get_one(self, box_id: int) -> Union[BoxInOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT u.first_name as subscriber_first_name, u.last_name as subscriber_last_name, u.id as subscriber_id
                        FROM boxes b
                        JOIN users u on u.id = b.subscriber_id
                        WHERE b.id = %s
                        """,
                        [box_id],
                    )
                    user_info = cur.fetchone()
                    subscriber_first_name = user_info[0]
                    subscriber_last_name = user_info[1]
                    subscriber_id = user_info[2]

                    cur.execute(
                        """
                        SELECT m.*
                        , u.first_name as chef_first_name
                        , u.last_name as chef_last_name
                        , bm.quantity
                        FROM box_meals bm
                        JOIN meals m ON m.id = bm.meal_id
                        JOIN boxes b ON b.id = bm.box_id
                        JOIN users u on u.id = m.chef_id
                        WHERE b.id = %s
                        """,
                        [box_id],
                    )
                    recs = cur.fetchall()
                    return BoxInOut(
                        box_id=box_id,
                        subscriber_id=subscriber_id,
                        subscriber_first_name=subscriber_first_name,
                        subscriber_last_name=subscriber_last_name,
                        meals=[
                            self.record_to_mealout_w_qty(rec) for rec in recs
                        ],
                    )
        except Exception as e:
            print(
                f"*********************************\nError Message:\n\n {e}\n*********************************"
            )
            return Error(message=str(e))

    def record_to_mealout_w_qty(self, record):
        return MealOutWQty(
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
            quantity=record[18],
        )
