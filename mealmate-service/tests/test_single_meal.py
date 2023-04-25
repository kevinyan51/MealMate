from fastapi.testclient import TestClient
from main import app
from queries.meal_details import MealDetailsRepository

client = TestClient(app)


test_meal = {
    "id": 1,
    "chef_id": 1,
    "name": "Test Meal",
    "name2": "This is a test meal",
    "created_at": "2021-01-01",
    "updated_at": "2021-01-01",
    "picture_url": "thisisatestpictureurl.com",
    "description": "this meal was designed to test",
    "instructions": "test the instructions",
    "ingredients": "test the ingredients",
    "calories": 400,
    "is_keto": True,
    "is_vegan": True,
    "is_chef_choice": True,
    "is_spicy": True,
    "has_cheese": True,
    "price": 1.00,
    "first_name": "Guy",
    "last_name": "fieri",
    "chef_picture_url": "insertcoolpicofguyfieri.here",
}


class SingleMealRepo:
    def get_one(self, id: int):
        return {
            "id": 1,
            **test_meal,
        }


def test_get_single_meal():
    app.dependency_overrides[MealDetailsRepository] = SingleMealRepo
    response = client.get("/api/meals/1/")
    app.dependecy_overrides = {}
    assert response.status_code == 200
    assert response.json() == {
        "id": 1,
        **test_meal,
    }
