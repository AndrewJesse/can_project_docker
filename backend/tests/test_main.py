# backend/tests/test_main.py

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_read_messages():
    response = client.get("/messages")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_message():
    new_message = {
        "arbitration_id": "test_id",
        "data": "test_data",
        "timestamp": "2024-07-24T00:00:00"
    }
    response = client.post("/messages", json=new_message)
    assert response.status_code == 200
    assert response.json()["arbitration_id"] == "test_id"

def test_db_check():
    response = client.get("/db-check")
    assert response.status_code == 200
    assert response.json()["status"] == "Database is connected"
