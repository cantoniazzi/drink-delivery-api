from fastapi.testclient import TestClient
import pytest

from app.api import app
from app.common.settings import settings
from app.models.distributor import Distributor


client = TestClient(app)
document_fixture = settings.get('distributor_document_fixture')


@pytest.mark.parametrize('clear_database', [[Distributor.document == document_fixture]], indirect=True)
def test_post_distributor_success(clear_database, get_distributor):
    response = client.post('/distributor/', json=get_distributor)

    distributor_response = response.json()

    assert response.status_code == 201
    assert distributor_response['address'] == get_distributor['address']
    assert distributor_response['coverage_area'] == get_distributor['coverage_area']
    assert distributor_response['document'] == get_distributor['document']
    assert distributor_response['owner_name'] == get_distributor['owner_name']
    assert distributor_response['trading_name'] == get_distributor['trading_name']


def test_post_distributor_error_with_invalid_address(get_distributor):
    distributor_payload = get_distributor
    distributor_payload['address'] = None

    response = client.post('/distributor/', json=distributor_payload)
    assert response.status_code == 422


def test_post_distributor_error_with_invalid_coverage_area(get_distributor):
    distributor_payload = get_distributor
    distributor_payload['coverage_area'] = None

    response = client.post('/distributor/', json=distributor_payload)
    assert response.status_code == 422


def test_post_distributor_error_with_invalid_document(get_distributor):
    distributor_payload = get_distributor
    distributor_payload['document'] = None

    response = client.post('/distributor/', json=distributor_payload)
    assert response.status_code == 422


def test_post_distributor_error_with_invalid_owner_name(get_distributor):
    distributor_payload = get_distributor
    distributor_payload['owner_name'] = None

    response = client.post('/distributor/', json=distributor_payload)
    assert response.status_code == 422


def test_post_distributor_error_with_invalid_trading_name(get_distributor):
    distributor_payload = get_distributor
    distributor_payload['trading_name'] = None

    response = client.post('/distributor/', json=distributor_payload)
    assert response.status_code == 422
