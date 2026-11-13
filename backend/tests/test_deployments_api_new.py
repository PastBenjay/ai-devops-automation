from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)



def test_health():
    response = client.get("/health")
    assert response.status_code == 200

    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["service"] == "ai-devops-automation-api"



def test_create_and_retrieve_deployment():
    response = client.post(
        "/api/deployments",
        json={"service": "web", "image": "nginx:stable", "environment": "dev"},
    )
    assert response.status_code == 201
    deployment = response.json()
    assert deployment["status"] == "pending"
    assert client.get(f"/api/deployments/{deployment['id']}").json() == deployment


def test_invalid_environment():
    response = client.post(
        "/api/deployments",
        json={"service": "web", "image": "nginx:stable", "environment": "unknown"},
    )
    assert response.status_code == 422


def test_missing_deployment():
    assert client.get("/api/deployments/999999").status_code == 404
