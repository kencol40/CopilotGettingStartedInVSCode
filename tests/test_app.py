import pytest
from fastapi.testclient import TestClient
from src.app import app

client = TestClient(app)

# Test GET /activities
def test_get_activities():
    # Arrange: nothing to set up
    # Act
    response = client.get("/activities")
    # Assert
    assert response.status_code == 200
    assert isinstance(response.json(), dict)

# Test POST /activities/{activity_name}/signup
def test_signup_for_activity():
    # Arrange
    activity = "Chess Club"
    email = "pytestuser@mergington.edu"
    # Act
    response = client.post(f"/activities/{activity}/signup?email={email}")
    # Assert
    assert response.status_code == 200 or response.status_code == 400
    if response.status_code == 200:
        assert f"Signed up {email}" in response.json()["message"]
    else:
        assert response.json()["detail"] == "Student already signed up"

# Placeholder for DELETE /activities/{activity_name}/unregister (not implemented yet)
@pytest.mark.skip(reason="Unregister endpoint not implemented yet")
def test_unregister_for_activity():
    # Arrange
    activity = "Chess Club"
    email = "pytestuser@mergington.edu"
    # Act
    response = client.delete(f"/activities/{activity}/unregister?email={email}")
    # Assert
    assert response.status_code in (200, 404, 400)
