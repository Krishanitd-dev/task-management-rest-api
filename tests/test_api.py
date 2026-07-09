from fastapi.testclient import TestClient
from task_api_app.main import app


client = TestClient(app)

def test_home():

    response = client.get("/")

    assert response.status_code == 200


def test_create_task():

    response = client.post(
        "/tasks",
        json={
            "title": "Learn Testing",
            "priority": 1
        }
    )

    assert response.status_code == 200
    assert response.json() == {"message": "Task created successfully"}


def test_invalid_task():

    response = client.post(
        "/tasks",
        json={}
    )

    assert response.status_code == 422

def test_get_task():

    response = client.get("/tasks")
        
    assert response.status_code == 200
    assert isinstance(response.json(), list)



def test_update_task():
    response = client.put(
        "/tasks/1",
        json={
            "title": "edit task",
            "priority": 1
        }
    )
    assert response.status_code == 200
    data = response.json()
    assert "message" in data
  


   

def test_delete_task():
    response = client.delete(
        "/tasks/1",
        
    )

    assert response.status_code == 200
    data = response.json()
    assert "message" in data

def test_health():

    response = client.get("/health")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"


def test_get_completed_task():
    response = client.get("/completed")

    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)

