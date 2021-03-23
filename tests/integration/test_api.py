from fastapi.testclient import TestClient

from app.api import app


client = TestClient(app)


def test_health_check_route():
    response = client.get('/healthcheck')
    assert response.status_code == 200


def test_metrics_route():
    response = client.get('/metrics')
    assert response.status_code == 200
