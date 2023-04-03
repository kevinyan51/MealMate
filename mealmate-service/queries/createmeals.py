from pydantic import BaseModel
from queries.pool import pool


class MealIn(BaseModel):
    name: str
    name2: str
    picture_url: str
    description: str
    instructions: str
    ingredients: str
    chef_id: int
    calories: int
    is_keto: bool
    is_vegan: bool
    is_chef_choice: bool
    is_spicy: bool
    has_cheese: bool
    price: int

class MealOut(BaseModel):
    id: int
    name: str
    name2: str
    picture_url: str
    description: str
    instructions: str
    ingredients: str
    chef_id: int
    calories: int
    is_keto: bool
    is_vegan: bool
    is_chef_choice: bool
    is_spicy: bool
    has_cheese: bool
    price: int

class Error(BaseModel):
    message:str

class MealRepository:
    def create(self, meals: MealIn) -> MealOut:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    result = db.execute(
                        """
                        INSERT INTO meals
                            (name, name2, picture_url, description, instructions, ingredients, chef_id, calories, is_keto, is_vegan, is_chef_choice, is_spicy, has_cheese)
                        VALUES
                            (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                        RETURNING id;
                        """,
                        [meals.name, meals.name2, meals.picture_url, meals.description, meals.instructions, meals.ingredients, meals.chef_id, meals.calories, meals.is_keto, meals.is_vegan, meals.is_chef_choice, meals.is_spicy, meals.has_cheese]
                    )
                    id = result.fetchone()[0]
                    old_data = meals.dict()
                    return MealOut(id=id, **old_data)
        except Exception as e:
            print(
                f"**\nError Message:\n\n {e}\n**"
            )
            return Error(message=str(e))
