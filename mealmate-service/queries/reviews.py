from pydantic import BaseModel
from typing import List, Optional, Union
from datetime import datetime
from queries.pool import pool
from queries.boxes import Error


class ReviewIn(BaseModel):
    subscriber_id: Optional[int]
    meal_id: Optional[int]
    rating: Optional[int]
    comment: Optional[str]


class ReviewOut(BaseModel):
    id: int
    review_status: str
    subscriber_id: int
    meal_id: int
    created_at: datetime
    updated_at: datetime
    rating: int
    comment: str
    reviewer_first_name: str
    reviewer_last_name: str


class ReviewRepo:
    def get_all(self) -> Union[List[ReviewOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT r.*, u.first_name, u.last_name 
                        FROM reviews r 
                        JOIN users u ON r.subscriber_id = u.id 
                        WHERE r.status_id = 6
                        """
                    )
                    recs = cur.fetchall()
                    return [self.record_to_review_out(rec) for rec in recs]

        except Exception as e:
            return Error(message=str(e))

    def create(self, review: ReviewIn) -> Union[ReviewOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO reviews (subscriber_id, meal_id, rating, comment)
                        VALUES (%s, %s, %s, %s) 
                        RETURNING id
                        """,
                        (
                            review.subscriber_id,
                            review.meal_id,
                            review.rating,
                            review.comment,
                        ),
                    )
                    review_id = cur.fetchone()[0]
                    cur.execute(
                        """
                        SELECT * FROM reviews WHERE id = %s
                        """,
                        (review_id),
                    )
                    rec = cur.fetchone()
                    return self.record_to_review_out(rec)

        except Exception as e:
            return Error(message=str(e))

    def get_all_by_user(self, user_id: int) -> Union[List[ReviewOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT r.*, u.first_name, u.last_name
                        FROM reviews r
                        JOIN users u ON r.subscriber_id = u.id
                        WHERE r.subscriber_id = %s
                        """,
                        (user_id,),
                    )
                    recs = cur.fetchall()
                    return [self.record_to_review_out(rec) for rec in recs]

        except Exception as e:
            return Error(message=str(e))

    def get_all_by_meal(self, meal_id: int) -> Union[List[ReviewOut], Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT r.*, u.first_name, u.last_name 
                        FROM reviews r
                        JOIN users u ON r.subscriber_id = u.id
                        WHERE r.meal_id = %s
                        """,
                        (meal_id,),
                    )
                    recs = cur.fetchall()
                    return [self.record_to_review_out(rec) for rec in recs]

        except Exception as e:
            return Error(message=str(e))

    def get_one(self, review_id: int) -> Union[ReviewOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        SELECT r.*, u.first_name, u.last_name 
                        FROM reviews r
                        JOIN users u ON r.subscriber_id = u.id
                        WHERE r.id = %s
                        """,
                        (review_id,),
                    )
                    rec = cur.fetchone()
                    if rec is None:
                        return Error(message="Review not found")
                    return self.record_to_review_out(rec)

        except Exception as e:
            return Error(message=str(e))

    def update(
        self, review_id: int, review: ReviewIn
    ) -> Union[ReviewOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        UPDATE reviews
                        SET rating = %s, comment = %s
                        WHERE id = %s
                        RETURNING id
                        """,
                        (
                            # review.subscriber_id,
                            # review.meal_id,
                            review.rating,
                            review.comment,
                            review_id,
                        ),
                    )
                    review_id = cur.fetchone()[0]
                    cur.execute(
                        """
                        SELECT r.*, u.first_name, u.last_name
                        FROM reviews r
                        JOIN users u ON r.subscriber_id = u.id
                        WHERE r.id = %s
                        """,
                        (review_id,),
                    )
                    rec = cur.fetchone()
                    return self.record_to_review_out(rec)

        except Exception as e:
            return Error(message=str(e))

    def delete(self, review_id: int) -> Union[ReviewOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        UPDATE reviews
                        SET status_id = 5
                        WHERE id = %s
                        RETURNING id
                        """,
                        (review_id,),
                    )
                    review_id = cur.fetchone()[0]
                    cur.execute(
                        """
                        SELECT r.*, u.first_name, u.last_name
                        FROM reviews r
                        JOIN users u ON r.subscriber_id = u.id
                        WHERE r.id = %s
                        """,
                        (review_id,),
                    )
                    rec = cur.fetchone()
                    if rec is None:
                        return Error(message="Review not found")
                    return self.record_to_review_out(rec)

        except Exception as e:
            return Error(message=str(e))

    def record_to_review_out(self, rec: tuple) -> ReviewOut:
        return ReviewOut(
            id=rec[0],
            review_status=rec[1],
            subscriber_id=rec[2],
            meal_id=rec[3],
            created_at=rec[4],
            updated_at=rec[5],
            rating=rec[6],
            comment=rec[7],
            reviewer_first_name=rec[8],
            reviewer_last_name=rec[9],
        )
