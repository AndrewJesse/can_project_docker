import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.main import app
from fastapi.testclient import TestClient

client = TestClient(app)

def test_read_messages():
    response = client.get("/api/messages")
    assert response.status_code == 200

def test_create_message():
    new_message = {
        "arbitration_id": "test_id",
        "data": "test_data",
        "timestamp": "2024-07-24T00:00:00"
    }
    response = client.post("/api/messages", json=new_message)
    assert response.status_code == 200

def test_db_check():
    response = client.get("/api/db-check")
    assert response.status_code == 200
