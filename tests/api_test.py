from fastapi.testclient import TestClient

from app.api import app


client = TestClient(app)


def test_health_check_route():
    response_base_path = client.get('/')
    response = client.get('/healthcheck')

    assert response_base_path.status_code == 200
    assert response.status_code == 200
