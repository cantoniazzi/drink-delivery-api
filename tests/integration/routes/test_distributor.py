from fastapi.testclient import TestClient
import pytest

from app.api import app
from app.common.settings import settings
from app.models.distributor import Distributor


client = TestClient(app)
document_fixture = settings.get('distributor_document_fixture')


@pytest.mark.parametrize('clear_database', [[Distributor.document == document_fixture]], indirect=True)
def test_get_distributor_error(clear_database):
    response = client.get('/distributor/123')
    assert response.status_code == 404


@pytest.mark.parametrize('clear_database', [[Distributor.document == document_fixture]], indirect=True)
def test_get_distributor_success(clear_database, get_distributor):
    post_response = client.post('/distributor/', json=get_distributor).json()
    get_response = client.get(f"/distributor/{post_response['id']}").json()

    assert get_response['address'] == get_distributor['address']
    assert get_response['coverage_area'] == get_distributor['coverage_area']
    assert get_response['document'] == get_distributor['document']
    assert get_response['owner_name'] == get_distributor['owner_name']
    assert get_response['trading_name'] == get_distributor['trading_name']


@pytest.mark.parametrize('clear_database', [[Distributor.document == document_fixture]], indirect=True)
def test_post_distributor_success(clear_database, get_distributor):
    response = client.post('/distributor/', json=get_distributor)
    response_distributor = response.json()

    assert response.status_code == 201
    assert response_distributor['address'] == get_distributor['address']
    assert response_distributor['coverage_area'] == get_distributor['coverage_area']
    assert response_distributor['document'] == get_distributor['document']
    assert response_distributor['owner_name'] == get_distributor['owner_name']
    assert response_distributor['trading_name'] == get_distributor['trading_name']


def test_post_distributor_error_with_invalid_address(get_distributor):
    get_distributor['address'] = None
    response = client.post('/distributor/', json=get_distributor)
    assert response.status_code == 422


def test_post_distributor_error_with_invalid_coverage_area(get_distributor):
    get_distributor['coverage_area'] = None
    response = client.post('/distributor/', json=get_distributor)
    assert response.status_code == 422


def test_post_distributor_error_with_invalid_document(get_distributor):
    get_distributor['document'] = None
    response = client.post('/distributor/', json=get_distributor)
    assert response.status_code == 422


def test_post_distributor_error_with_invalid_owner_name(get_distributor):
    get_distributor['owner_name'] = None
    response = client.post('/distributor/', json=get_distributor)
    assert response.status_code == 422


def test_post_distributor_error_with_invalid_trading_name(get_distributor):
    get_distributor['trading_name'] = None
    response = client.post('/distributor/', json=get_distributor)
    assert response.status_code == 422
