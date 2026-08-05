import pytest
from fastapi.testclient import TestClient
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import app, activities

client = TestClient(app)


@pytest.fixture(autouse=True)
def reset_activities():
    """Reset activities to a clean state before each test."""
    original = {
        name: {**details, "participants": list(details["participants"])}
        for name, details in activities.items()
    }
    yield
    activities.clear()
    activities.update(original)


def test_get_activities():
    response = client.get("/activities")
    assert response.status_code == 200
    data = response.json()
    assert "Chess Club" in data
    assert len(data) >= 4


def test_signup_for_activity():
    response = client.post("/activities/Chess Club/signup?email=test@mergington.edu")
    assert response.status_code == 200
    assert "test@mergington.edu" in response.json()["message"]


def test_signup_duplicate_raises_error():
    client.post("/activities/Chess Club/signup?email=dup@mergington.edu")
    response = client.post("/activities/Chess Club/signup?email=dup@mergington.edu")
    assert response.status_code == 400
    assert "already signed up" in response.json()["detail"]


def test_signup_nonexistent_activity():
    response = client.post("/activities/Nonexistent/signup?email=a@mergington.edu")
    assert response.status_code == 404


def test_unregister_from_activity():
    client.post("/activities/Chess Club/signup?email=remove@mergington.edu")
    response = client.delete("/activities/Chess Club/signup?email=remove@mergington.edu")
    assert response.status_code == 200
    assert "remove@mergington.edu" in response.json()["message"]


def test_unregister_not_signed_up():
    response = client.delete("/activities/Chess Club/signup?email=nobody@mergington.edu")
    assert response.status_code == 400


def test_unregister_nonexistent_activity():
    response = client.delete("/activities/Nonexistent/signup?email=a@mergington.edu")
    assert response.status_code == 404
