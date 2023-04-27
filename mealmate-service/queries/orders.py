from pydantic import BaseModel
from typing import List, Union
from datetime import datetime
from queries.pool import pool
from queries.boxes import Error


class MealOutInOrder(BaseModel):
    order_id: int
    order_status: str
    order_created_at: datetime
    order_updated_at: datetime
    subscriber_id: int
    meal_id: int
    meal_name: str
    meal_name2: str
    meal_price: float
    meal_picture_url: str
    quantity: int


class OrderIn(BaseModel):
    order_id: int
    order_status: str


class OrderOut(BaseModel):
    order_id: int
    order_status: str
    order_created_at: datetime
    order_updated_at: datetime
    subscriber_id: int
    num_meals: int
    total_price: float
    meals: List[MealOutInOrder]


class OrderRepo:
    def create(self, box_id: int) -> Union[OrderOut, Error]:
        print("---------------------------------")
        print("box_id", box_id)
        print("---------------------------------")
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO orders
                        (subscriber_id, status_id)
                        VALUES
                        (
                            (
                                SELECT b.subscriber_id FROM boxes b
                                JOIN users u on b.subscriber_id = u.id
                                WHERE b.id = %s
                                LIMIT 1
                            )
                            , 1
                        )
                        RETURNING id;
                        """,
                        [box_id],
                    )
                    order_id = cur.fetchone()[0]
                    cur.execute(
                        """
                        INSERT INTO order_meals
                        (order_id, meal_id, quantity)
                        SELECT
                          %s
                          , meal_id
                          , quantity
                        FROM box_meals
                        WHERE box_id = %s
                        ;
                        """,
                        [order_id, box_id],
                    )
                    cur.execute(
                        """
                        DELETE FROM box_meals
                        WHERE box_id = %s
                        ;
                        """,
                        [box_id],
                    )
                    cur.execute(
                        """
                        SELECT o.id
                          , s.name
                          , o.created_at
                          , o.updated_at
                          , o.subscriber_id
                          , m.id
                          , m.name
                          , m.name2
                          , m.price
                          , m.picture_url
                          , om.quantity
                        FROM orders o
                        JOIN order_meals om on o.id = om.order_id
                        JOIN meals m on om.meal_id = m.id
                        JOIN statuses s on o.status_id = s.id
                        WHERE o.id = %s
                        """,
                        [order_id],
                    ),
                    recs = cur.fetchall()
                    lst_mealout = [
                        self.record_to_meal_out(rec) for rec in recs
                    ]
                    lst_orderout = self.meal_out_to_order_out(lst_mealout)
                    return lst_orderout[0]
        except Exception as e:
            # print(f"******\nError Message:\n\n {e}\n******")
            return Error(message=str(e))

    def get_all_by_user(self, user_id: int) -> Union[List[OrderOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT o.id
                          , s.name
                          , o.created_at
                          , o.updated_at
                          , o.subscriber_id
                          , m.id
                          , m.name
                          , m.name2
                          , m.price
                          , m.picture_url
                          , om.quantity
                        FROM orders o
                        JOIN order_meals om on o.id = om.order_id
                        JOIN meals m on om.meal_id = m.id
                        JOIN statuses s on o.status_id = s.id
                        WHERE o.subscriber_id = %s
                        """,
                        [user_id],
                    )
                    recs = cur.fetchall()
                    lst_mealout = [
                        self.record_to_meal_out(rec) for rec in recs
                    ]
                    lst_orderout = self.meal_out_to_order_out(lst_mealout)
                    return lst_orderout

        except Exception as e:
            # print(f"******\nError Message:\n\n {e}\n******")
            return Error(message=str(e))

    def get_all(self) -> Union[List[OrderOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT o.id
                          , s.name
                          , o.created_at
                          , o.updated_at
                          , o.subscriber_id
                          , m.id
                          , m.name
                          , m.name2
                          , m.price
                          , m.picture_url
                          , om.quantity
                        FROM orders o
                        JOIN order_meals om on o.id = om.order_id
                        JOIN meals m on om.meal_id = m.id
                        JOIN statuses s on o.status_id = s.id
                        """,
                    )
                    recs = cur.fetchall()
                    lst_mealout = [
                        self.record_to_meal_out(rec) for rec in recs
                    ]
                    lst_orderout = self.meal_out_to_order_out(lst_mealout)
                    return lst_orderout

        except Exception as e:
            # print(f"******\nError Message:\n\n {e}\n******")
            return Error(message=str(e))

    def get_one(self, order_id: int) -> Union[OrderOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                      SELECT o.id
                          , s.name
                          , o.created_at
                          , o.updated_at
                          , o.subscriber_id
                          , m.id
                          , m.name
                          , m.name2
                          , m.price
                          , m.picture_url
                          , om.quantity
                        FROM orders o
                        JOIN order_meals om on o.id = om.order_id
                        JOIN meals m on om.meal_id = m.id
                        JOIN statuses s on o.status_id = s.id
                        WHERE o.id = %s
                      """,
                        [order_id],
                    )
                    recs = cur.fetchall()
                    lst_mealout = [
                        self.record_to_meal_out(rec) for rec in recs
                    ]
                    lst_orderout = self.meal_out_to_order_out(lst_mealout)
                    return lst_orderout[0]

        except Exception as e:
            # print(f"******\nError Message:\n\n {e}\n******")
            return Error(message=str(e))

    def update(self, order_id: int, order_in: OrderIn) -> Union[dict, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        UPDATE orders
                        SET status_id = %s
                        WHERE id = %s
                        """,
                        [order_in.status_id, order_id],
                    )
                    return {"message": "Order updated successfully"}
                    # cur.execute(
                    #     """
                    #     SELECT o.id
                    #       , s.name
                    #       , o.created_at
                    #       , o.updated_at
                    #       , o.subscriber_id
                    #       , m.id
                    #       , m.name
                    #       , m.name2
                    #       , m.price
                    #       , m.picture_url
                    #       , om.quantity
                    #     FROM orders o
                    #     JOIN order_meals om on o.id = om.order_id
                    #     JOIN meals m on om.meal_id = m.id
                    #     JOIN statuses s on o.status_id = s.id
                    #     WHERE o.id = %s
                    #     """,
                    #     [order_id],
                    # )
                    # recs = cur.fetchall()
                    # lst_mealout = [
                    #     self.record_to_meal_out(rec) for rec in recs
                    # ]
                    # lst_orderout = self.meal_out_to_order_out(lst_mealout)
                    # return lst_orderout[0]

        except Exception as e:
            # print(f"******\nError Message:\n\n {e}\n******")
            return Error(message=str(e))

    def delete(self, order_id: int) -> Union[OrderOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        UPDATE orders
                        SET status_id = 5
                        WHERE id = %s
                        RETURNING *
                        """,
                        [order_id],
                    )
                    rec = cur.fetchone()
                    if rec is None:
                        return Error(message="Order not found")
                    lst_mealout = [self.record_to_meal_out(rec)]
                    lst_orderout = self.meal_out_to_order_out(lst_mealout)
                    return lst_orderout[0]

        except Exception as e:
            # print(f"******\nError Message:\n\n {e}\n******")
            return Error(message=str(e))

    def meal_out_to_order_out(self, lst_mealout):
        dct_ords = {}
        for mealout in lst_mealout:
            order_id = mealout.order_id
            if dct_ords.get(order_id):
                dct_ords[order_id].num_meals += mealout.quantity
                dct_ords[order_id].total_price += (
                    mealout.meal_price * mealout.quantity
                )
                dct_ords[order_id].meals.append(mealout)
            else:
                dct_ords[order_id] = OrderOut(
                    order_id=order_id,
                    order_status=mealout.order_status,
                    order_created_at=mealout.order_created_at,
                    order_updated_at=mealout.order_updated_at,
                    subscriber_id=mealout.subscriber_id,
                    num_meals=mealout.quantity,
                    total_price=mealout.meal_price * mealout.quantity,
                    meals=[mealout],
                )
        return list(dct_ords.values())

    def if_ordered_meal(
        self, meal_id: int, user_id: int
    ) -> Union[bool, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT *
                        FROM order_meals om
                        JOIN orders o on om.order_id = o.id
                        WHERE meal_id = %s AND subscriber_id = %s
                        """,
                        (meal_id, user_id),
                    )
                    rec = cur.fetchone()
                    if rec is None:
                        return False
                    return True

        except Exception as e:
            return Error(message=str(e))

    def record_to_meal_out(self, record):
        return MealOutInOrder(
            order_id=record[0],
            order_status=record[1],
            order_created_at=record[2],
            order_updated_at=record[3],
            subscriber_id=record[4],
            meal_id=record[5],
            meal_name=record[6],
            meal_name2=record[7],
            meal_price=record[8],
            meal_picture_url=record[9],
            quantity=record[10],
        )
