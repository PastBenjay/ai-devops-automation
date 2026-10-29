from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["service"] == "ai-devops-automation-api"


def test_api_health_endpoint():
    response = client.get("/api/health")
    assert response.status_code == 200
    payload = response.json()
    assert payload["status"] == "ok"
    assert payload["checks"]["database"] == "ok"


def test_deployments_endpoint():
    response = client.get("/api/deployments")
    assert response.status_code == 200
    payload = response.json()
    assert payload["count"] >= 1
    assert len(payload["deployments"]) == payload["count"]
