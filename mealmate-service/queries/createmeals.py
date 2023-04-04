from pydantic import BaseModel
from queries.pool import pool
from typing import Union

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

    def update_meal(self, meal_id: int, meal:MealIn) -> Union[MealOut, Error]:
        try:
            with pool.connection() as conn:
                with conn.cursor() as db:
                    db.execute(
                        '''
                        UPDATE meals
                        SET name = %s, name2 = %s, picture_url = %s, description = %s, instructions = %s, ingredients = %s, chef_id = %s, calories = %s, is_keto = %s, is_vegan = %s, is_chef_choice = %s, is_spicy = %s, has_cheese = %s
                        WHERE id = %s
                        ''',
                        [
                        meal.name, meal.name2, meal.picture_url, meal.description, meal.instructions, meal.ingredients, meal.chef_id, meal.calories, meal.is_keto, meal.is_vegan, meal.is_chef_choice, meal.is_spicy, meal.has_cheese, meal_id
                        ]
                    )
                    return self.meal_in_to_out(meal_id, meal)
        except Exception as e:
            print(e)
            return {"message" : "Could not update meal"}

    def meal_in_to_out(self, id:int, meal:MealIn):
        old_data = meal.dict()
        return MealOut(id=id, **old_data)
