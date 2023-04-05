from pydantic import BaseModel
from typing import List
from queries.pool import pool


class AccountForm(BaseModel):
    username: str
    password: str


class DuplicationAccountError(ValueError):
    pass


class UserIn(BaseModel):
    role_id: int
    first_name: str
    last_name:str
    username: str
    email: str
    password: str
    picture_url:str


class UserOut(BaseModel):
    id: int
    role_id: int
    first_name: str
    last_name:str
    username: str
    email: str
    hashed_password: str
    picture_url: str


class UserOutLess(BaseModel):
    id: int
    username: str


class UserOutWithPassword(UserOut):
    hashed_password: str


class Error(BaseModel):
    message: str


class Userlogout(BaseModel):
    id: str
    username: str
    password: str
    token: str


class UserRepository:
    def create(
        self, user: UserIn, hashed_password: str
    ) -> UserOutWithPassword:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    existing_user = self.get(user.username)
                    if existing_user:
                        raise DuplicationAccountError(
                            "User with this email already exists"
                        )
                    result = db.execute(
                        """
                            INSERT INTO users
                                (role_id,
                                first_name,
                                last_name,
                                username,
                                email,
                                hashed_password,
                                created_at,
                                picture_url)
                            VALUES
                                (%s, %s, %s, %s, %s, %s, NOW(), %s)
                            RETURNING id;
                        """,
                        [
                            user.role_id,
                            user.first_name,
                            user.last_name,
                            user.username,
                            user.email,
                            hashed_password,
                            user.picture_url
                        ],
                    )
                    id = result.fetchone()[0]
                    old_data = user.dict()
                    return UserOutWithPassword(
                        id=id, **old_data, hashed_password=hashed_password
                    )
        except DuplicationAccountError as e:
            raise e
        except Exception:
            return {"message": "Create did not work"}

    def update(self, user_id: int, user: UserIn) -> UserOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                            UPDATE users
                            SET username = %s
                                , email =  %s
                                , hashed_password = %s
                            WHERE id =  %s
                        """,
                        [user.username, user.email, user.password, user_id],
                    )
                    return self.user_into_out(user_id, user)
        except Exception as e:
            print(e)
            return {"User has not been updated"}

    def delete(self, user_id: int) -> bool:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                            DELETE FROM users
                            WHERE id = %s
                            RETURNING id
                        """,
                        [user_id],
                    )
                    id = result.fetchone()[0]
                    return {f"User {id} deleted": True}
        except Exception as e:
            print(e)
            return {"User deleted": False}

    def get(self, username: str) -> UserOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        SELECT id, role_id, username, email, hashed_password
                        FROM users
                        WHERE username = %s
                        """,
                        [username],
                    )
                    record = result.fetchone()
                    if record is None:
                        return None
                    user = UserOut(
                        id=record[0],
                        role_id=record[1],
                        username=record[2],
                        email=record[3],
                        hashed_password=record[4],
                    )
                    return user
        except Exception as e:
            print(e)
            return {"message": "Could not get user"}

    def get_all(self) -> List[UserOut]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        """
                            SELECT id, role_id, username, email, hashed_password
                            FROM users
                        """
                    )
                    result = db.fetchall()
                    return [
                        UserOut(
                            id=id,
                            role_id=role_id,
                            username=username,
                            email=email,
                            hashed_password=hashed_password
                        )
                        for id, role_id, username, email, hashed_password in result
                    ]
        except Exception as e:
            print(e)
            return {"Users not found"}

    def user_into_out(self, id: id, user: UserOut):
        old_data = user.dict()
        return UserOut(id=id, **old_data)
