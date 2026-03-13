from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

def test_get_activities():
    # Arrange: No setup needed

    # Act
    response = client.get("/activities")

    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)
    assert "Chess Club" in response.json()

def test_signup_for_activity_success():
    # Arrange
    activity = "Chess Club"
    email = "newuser@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 200
    assert response.json()["message"].startswith("Signed up")

def test_signup_for_activity_duplicate():
    # Arrange
    activity = "Chess Club"
    email = "newuser@mergington.edu"

    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")

    # Assert
    assert response.status_code == 400
    assert response.json()["detail"] == "Student already signed up"

def test_unregister_from_activity():
    # Arrange
    activity = "Chess Club"
    email = "newuser@mergington.edu"

    # Act
    response = client.delete(f"/activities/{activity}/unregister?email={email}")

    # Assert
    assert response.status_code == 200
    assert response.json()["message"].startswith("Unregistered")
