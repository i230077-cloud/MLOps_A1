from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_health_endpoint():
    """Test 1: Health Endpoint validation"""
    response = client.get("/health")
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "healthy"
    assert data["application"] == "student-ml-api"
    assert "version" in data



def test_predict_success():
    """Test 2: Successful /predict calculation"""
    response = client.post("/predict", json={"value": 10})
    assert response.status_code == 200
    data = response.json()
    assert data["input"] == 10
    assert data["prediction"] == 20

def test_predict_missing_input():
    """Test 3: Missing input validation failure"""
    response = client.post("/predict", json={})
    assert response.status_code == 422  # FastAPI validation error status code

def test_predict_invalid_input():
    """Test 4: Invalid input type validation failure"""
    response = client.post("/predict", json={"value": "not_a_number"})
    assert response.status_code == 422
