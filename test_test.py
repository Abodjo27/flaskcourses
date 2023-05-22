from flask import Flask
from json_saver import JsonSaver
import pytest
import uuid

from app import app



@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_home_page(client):
    response = client.get("/")
    assert response.status_code == 200


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
    
def test_json_saver():
    json_saver = JsonSaver("test_datass.json")
    # Ajouter des données de test dans le fichier JSON
    data1 = {
        "id": str(uuid.uuid4()),
        "title": "Test Todo 1",
        "description": "This is test todo 1",
        "status": 0,
        "due": "2023-01-01",
    }
    json_saver.add(data1["id"], data1)

    data2 = {
        "id": str(uuid.uuid4()),
        "title": "Test Todo 2",
        "description": "This is test todo 2",
        "status": 1,
        "due": "2023-01-02",
    }
    json_saver.add(data2["id"], data2)

    # Utiliser JsonSaver pour lire les données du fichier JSON
    todos = json_saver.find_all()

    # Vérifier que les données sont correctement lues
    assert len(todos) == 2
    assert todos[0]["title"] == "Test Todo 1"
    assert todos[0]["description"] == "This is test todo 1"
    assert todos[0]["status"] == 0
    assert todos[0]["due"] == "2023-01-01"
    assert todos[1]["title"] == "Test Todo 2"
    assert todos[1]["description"] == "This is test todo 2"
    assert todos[1]["status"] == 1
    assert todos[1]["due"] == "2023-01-02"



def test_get_todos(client):
    response = client.get("/todos")
    assert response.status_code == 200


if __name__ == "__main__":
    pytest.main()
