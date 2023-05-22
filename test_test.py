from flask import Flask
import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"todoapp" in response.data


def test_create_todos(client):
    response = client.post(
        "/todos",
        json={
            "title": "Test Todo",
            "description": "This is a test todo",
            "status": 0,
            "due": "2023-01-01",
        },
    )
    assert response.status_code == 302  # Redirect
    assert response.headers["Location"] == "http://localhost/todos"


def test_get_todos(client):
    response = client.get("/todos")
    assert response.status_code == 200
    assert b"Test Todo" in response.data


if __name__ == "__main__":
    pytest.main()
