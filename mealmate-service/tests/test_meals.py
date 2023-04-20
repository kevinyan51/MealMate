from fastapi.testclient import TestClient
from main import app
from queries.meals import MealRepo

client = TestClient(app)


dummy_meal = {
    "status_id": 1,
    "chef_id": 1,
    "name": "Test Meal",
    "name2": "Test Meal 2",
    "created_at": "2021-01-01T00:00:00",
    "updated_at": "2021-01-01T00:00:00",
    "picture_url": "https://www.google.com",
    "description": "Test Description",
    "instructions": "Test Instructions",
    "ingredients": "Test Ingredients",
    "calories": 100,
    "is_keto": True,
    "is_vegan": True,
    "is_chef_choice": True,
    "is_spicy": True,
    "has_cheese": True,
    "price": 10.00,
    "chef_first_name": "Test",
    "chef_last_name": "Chef",
    "chef_picture_url": "https://www.google.com",
}


class EmptyMealsRepo:
    def get_all(self):
        return []

    def get_all_by_user(self, user_id: int):
        return []


class DummyMealsRepo:
    def get_all(self):
        return [
            {
                "meal_id": 1,
                **dummy_meal,
            },
            {
                "meal_id": 2,
                **dummy_meal,
            },
        ]

    def get_all_by_user(self, user_id: int):
        result = [{"meal_id": 1, **dummy_meal}]
        return result


def test_get_all_meals():
    app.dependency_overrides[MealRepo] = DummyMealsRepo
    response = client.get("/api/meals/")
    app.dependency_overrides = {}

    assert response.status_code == 200
    assert response.json() == [
        {
            "meal_id": 1,
            **dummy_meal,
        },
        {
            "meal_id": 2,
            **dummy_meal,
        },
    ]


def test_get_user_meals():
    app.dependency_overrides[MealRepo] = DummyMealsRepo
    response = client.get("/api/users/1/meals/")
    app.dependency_overrides = {}
    assert response.status_code == 200
    assert response.json() == [
        {
            "meal_id": 1,
            **dummy_meal,
        }
    ]


def test_get_empty_meals():
    app.dependency_overrides[MealRepo] = EmptyMealsRepo
    response = client.get("/api/meals/")
    app.dependency_overrides = {}
    assert response.status_code == 200
    assert response.json() == []


def test_get_empty_user_meals():
    app.dependency_overrides[MealRepo] = EmptyMealsRepo
    response = client.get("/api/users/1/meals/")
    app.dependency_overrides = {}
    assert response.status_code == 200
    assert response.json() == []
