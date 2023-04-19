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
            # print(
            # f"******\nError Message:\n\n {e}\n******"
            # )
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
            # print(f"******\nError Message:\n\n {e}\n******")
            return Error(message=str(e))

    def get_one(self, box_id: int) -> Union[BoxInOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT u.first_name as subscriber_first_name
                            , u.last_name as subscriber_last_name
                            , u.id as subscriber_id
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
                        , u.picture_url as chef_picture_url
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
            # print(
            # f"******\nError Message:\n\n {e}\n******"
            # )
            return Error(message=str(e))

    def record_to_mealout_w_qty(self, record):
        return MealOutWQty(
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
            quantity=record[21],
        )
