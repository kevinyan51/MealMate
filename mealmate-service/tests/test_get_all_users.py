from fastapi.testclient import TestClient
from main import app
from queries.users import UserQueries

client = TestClient(app)

dummy_user = {
    "id": 1,
    "first_name": "Jill",
    "last_name": "Dill",
    "username": "jilldill",
    "email": "jd@mm.com",
    "picture_url": "",
    "role_id": 1,
    "hashed_password": "strongestpassword"
}


class MockUserQuerie:
    def get_all_users(self):
        return [dummy_user]


def test_get_all_users():
    app.dependency_overrides[UserQueries] = MockUserQuerie
    response = client.get("/api/users/")
    app.dependency_overrides = {}
    assert response.status_code == 200
    assert response.json() == [dummy_user]
