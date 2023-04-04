from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import datetime
from queries.pool import pool
from queries.boxes import MealOutWQty, Error


class OrderOut(BaseModel):
    order_id: int
    order_created_at: datetime
    order_updated_at: datetime
    num_meals: Optional[int]
    total_price: Optional[float]
    meals: List[MealOutWQty]


class SingleOrderMealOut(MealOutWQty):
    order_id: int
    order_created_at: datetime
    order_updated_at: datetime


class OrderRepo:
    def get_all_by_user(self, user_id: int) -> Union[List[OrderOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT o.id
                          , o.created_at
                          , o.updated_at
                          , m.*
                          , om.quantity
                        FROM orders o
                        JOIN order_meals om on o.id = om.order_id
                        JOIN meals m on om.meal_id = m.id
                        JOIN users u on o.subscriber_id = u.id
                        WHERE o.subscriber_id = %s
                        """,
                        [user_id],
                    )
                    recs = cur.fetchall()
                    if recs == []:
                        return Error(message="No orders found.")
                    else:
                        print("-------------------------------------------")
                        print("records", recs)
                        print("-------------------------------------------")
                        res = [self.record_to_order_out(rec) for rec in recs]
                        res = [self.parse_records_to_order_out(res)]
                        return [self.add_total_price(v) for v in res]

        except Exception as e:
            print(
                f"*********************************\nError Message:\n\n {e}\n*********************************"
            )
            return Error(message=str(e))

    def parse_records_to_order_out(self, records):
        res = {}
        for record in records:
            order_id = record.order_id
            if res[order_id]:
                res[order_id].meals.append(record)
            else:
                res[order_id] = OrderOut(
                    order_id=order_id,
                    order_created_at=record.order_created_at,
                    order_updated_at=record.order_updated_at,
                    num_meals=1,
                    meals=[record],
                )
        result = [self.add_total_price(v) for v in res.values()]
        return result

    def add_total_price(self, order: OrderOut):
        total_price = 0
        for meal in order.meals:
            total_price += meal.price * meal.quantity
        return OrderOut(
            order_id=order.order_id,
            order_created_at=order.order_created_at,
            order_updated_at=order.order_updated_at,
            num_meals=len(order.meals),
            total_price=total_price,
            meals=order.meals,
        )

    def record_to_order_out(self, record):
        return SingleOrderMealOut(
            order_id=record[0],
            order_created_at=record[1],
            order_updated_at=record[2],
            meal_id=record[3],
            chef_id=record[4],
            name=record[5],
            name2=record[6],
            created_at=record[7],
            updated_at=record[8],
            picture_url=record[9],
            description=record[10],
            instructions=record[11],
            ingredients=record[12],
            calories=record[13],
            is_keto=record[14],
            is_vegan=record[15],
            is_chef_choice=record[16],
            is_spicy=record[17],
            has_cheese=record[18],
            price=record[19],
            quantity=record[20],
        )
