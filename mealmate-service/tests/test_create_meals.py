from fastapi.testclient import TestClient
from main import app
from queries.createmeals import MealRepository, MealIn, MealOut

client = TestClient(app)

dummy_meal = {
    "name": "Test Meal",
    "name2": "Test Meal2",
    "picture_url": "testingtesting",
    "description": "Test Description",
    "instructions": "Test Instructions",
    "ingredients": "Test Ingredients",
    "chef_id": 2,
    "calories": 100,
    "is_keto": True,
    "is_vegan": True,
    "is_chef_choice": True,
    "is_spicy": True,
    "has_cheese": True,
    "price": 10.00,
}

class DummyMealsRepoCreate:
    def create(self, meal: MealIn):
        return MealOut(
            id=500,
            name=meal.name,
            name2=meal.name2,
            picture_url=meal.picture_url,
            description=meal.description,
            instructions=meal.instructions,
            ingredients=meal.ingredients,
            chef_id=meal.chef_id,
            calories=meal.calories,
            is_keto=meal.is_keto,
            is_vegan=meal.is_vegan,
            is_chef_choice=meal.is_chef_choice,
            is_spicy=meal.is_spicy,
            has_cheese=meal.has_cheese,
            price=meal.price,
        )

def test_create_meal():
    app.dependency_overrides[MealRepository] = DummyMealsRepoCreate
    response = client.post('/api/meals/', json=dummy_meal)
    app.dependency_overrides = {}
    assert response.status_code == 200
    assert response.json() == {
        "id": 500,
        "name": "Test Meal",
        "name2": "Test Meal2",
        "picture_url": "testingtesting",
        "description": "Test Description",
        "instructions": "Test Instructions",
        "ingredients": "Test Ingredients",
        "chef_id": 2,
        "calories": 100,
        "is_keto": True,
        "is_vegan": True,
        "is_chef_choice": True,
        "is_spicy": True,
        "has_cheese": True,
        "price": 10.00,
    }
