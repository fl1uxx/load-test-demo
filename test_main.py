
import pytest
from unittest.mock import Mock
from fastapi.testclient import TestClient
import main


@pytest.fixture
def client():
    with TestClient(main.app) as test_client:
        yield test_client


# 1. Unit Testing: API тесттері

def test_root_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}


def test_users_endpoint(client):
    response = client.get("/users")
    assert response.status_code == 200
    assert len(response.json()) == 10


def test_health_endpoint(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"


# 2. TDD: Positive және Negative тесттері

@pytest.mark.parametrize(
    "username, expected",
    [
        ("admin123", True),
        ("user2026", True),
        ("ab", False),
        ("admin@123", False),
        ("", False),
        (None, False),
    ]
)
def test_username_validation(username, expected):
    assert main.is_valid_username(username) is expected


# 3. Fixture және Exception

def test_fixture(client):
    assert client.get("/health").status_code == 200


def test_exception():
    with pytest.raises(ZeroDivisionError):
        1 / 0


# 4. Skip

@pytest.mark.skip(reason="Болашақ функционал")
def test_future_feature():
    assert True


# 5. Mock және Stub

def test_mock_user():
    mock_api = Mock()
    mock_api.get_user.return_value = {
        "id": 99,
        "name": "MockUser"
    }

    result = mock_api.get_user(99)

    assert result["name"] == "MockUser"
    mock_api.get_user.assert_called_once_with(99)


def test_stub_user():
    class UserStub:
        def get_user(self, user_id):
            return {"id": user_id, "name": "StubUser"}

    stub = UserStub()
    result = stub.get_user(1)

    assert result["name"] == "StubUser"
