from pydantic import BaseModel
from typing import List, Optional
from queries.pool import pool


class UserIn(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: str
    password: str
    picture_url: str
    role_id: int


class UserOut(BaseModel):
    id: int
    first_name: str
    last_name: str
    username: str
    email: str
    picture_url: str
    role_id: int


class UserOutWithPassword(UserOut):
    hashed_password: str


class Error(BaseModel):
    message: str


class UserQueries:
    # ####CREATE USER#####
    def create(
        self, user: UserIn, hashed_password: str
    ) -> UserOutWithPassword:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        INSERT INTO users
                            (
                                first_name,
                                last_name,
                                username,
                                email,
                                hashed_password,
                                picture_url,
                                role_id
                            )
                        VALUES
                            (%s, %s, %s, %s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [
                            user.first_name,
                            user.last_name,
                            user.username,
                            user.email,
                            hashed_password,
                            user.picture_url,
                            user.role_id,
                        ],
                    )
                    id = db.fetchone()[0]
                    old_data = user.dict()
                    old_data["hashed_password"] = hashed_password
                    return UserOutWithPassword(
                        id=id,
                        **old_data,
                    )
        except Exception as e:
            if "username" in str(e):
                raise ValueError("Cannot use username")
            elif "email" in str(e):
                raise ValueError("Cannot use email")
            else:
                raise e

    # ####GET USER FOR AUTHENTICATOR#####
    def get(self, username: str) -> Optional[UserOutWithPassword]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                            , first_name
                            , last_name
                            , username
                            , email
                            , hashed_password
                            , picture_url
                            , role_id
                        FROM users
                        WHERE username = %s
                        """,
                        [username],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_to_user_out(record)
        except Exception as e:
            print(e)
            return {"message": "Cannot get user"}

    # ####GET USER BY ID#####
    def get_user(self, id: int) -> Optional[UserOutWithPassword]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id
                            , first_name
                            , last_name
                            , username
                            , email
                            , hashed_password
                            , picture_url
                            , role_id
                        FROM users
                        WHERE id = %s
                        """,
                        [id],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    return self.record_to_user_out(record)
        except Exception as e:
            print(e)
            return {"message": "Cannot get user"}

    # ####GET ALL USERS#####
    def get_all_users(self) -> List[UserOutWithPassword]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as cur:
                    result = cur.execute(
                        """
                        SELECT id
                            , first_name
                            , last_name
                            , username
                            , email
                            , hashed_password
                            , picture_url
                            , role_id
                        FROM users
                        ORDER BY id;
                        """
                    )
                    records = result.fetchall()
                    return [
                        self.record_to_user_out(record) for record in records
                    ]
        except Exception as e:
            print(e)
            return {"message": "Cannot get all users"}

    # ####UPDATE USER#####
    def update_user(
        self, id: int, user: UserIn
    ) -> Optional[UserOutWithPassword]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        UPDATE users
                        SET first_name = %s
                          , last_name = %s
                          , username = %s
                          , email = %s
                          , picture_url = %s
                        WHERE id = %s
                        RETURNING id, first_name, last_name, username, email,
                            hashed_password, picture_url, role_id
                        """,
                        [
                            user.first_name,
                            user.last_name,
                            user.username,
                            user.email,
                            user.picture_url,
                            id,
                        ],
                    )
                    record = db.fetchone()
                    # print(record)
                    return self.record_to_user_update(record)
        except Exception as e:
            print(e)
            return {"message": "Cannot update user"}

    # ####DELETE USER#####
    def delete_user(self, id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                        DELETE FROM users
                        WHERE id = %s;
                        """,
                        [id],
                    )
                    return True
        except Exception as e:
            print(e)
            return {"message": "Cannot delete user"}

    # ####ENCODERS#####

    def record_to_user_out(self, record):
        return UserOutWithPassword(
            id=record[0],
            first_name=record[1],
            last_name=record[2],
            username=record[3],
            email=record[4],
            hashed_password=record[5],
            picture_url=record[6],
            role_id=record[7],
        )

    def record_to_user_update(self, record):
        return UserOutWithPassword(
            id=record[0],
            first_name=record[1],
            last_name=record[2],
            username=record[3],
            email=record[4],
            hashed_password=record[5],
            picture_url=record[6],
            role_id=record[7],
        )
