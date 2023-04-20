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
    "hashed_password": "strongestpassword",
    "picture_url": "",
    "role_id": 1
}


class MockUserQuerie:
    def get_user(self, username):
        return [dummy_user] if username == dummy_user["username"] else None


def test_get_user():
    app.dependency_overrides[UserQueries] = MockUserQuerie
    response = client.get("/users/")
    assert response.status_code == 200
    app.dependency_overrides = {}
