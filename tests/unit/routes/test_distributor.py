from unittest.mock import patch, Mock

from fastapi import HTTPException
import pytest

from app.routes.distributor import create_distributor
from app.routes.distributor import get_distributor_by_id
from app.routes.distributor import get_distributor_by_lat_long
from app.schemas.distributor import DistributorBaseSchema


def test_get_distributor_by_id_error_404(get_distributor):
    with patch('app.routes.distributor.get_db') as mock_db_session:
        id = 1234
        mock_db_session.query.return_value.filter.return_value = None

        with pytest.raises(HTTPException):
            get_distributor_by_id(id, mock_db_session)


def test_get_distributor_by_id_error_500(get_distributor):
    with patch('app.routes.distributor.get_db') as mock_db_session:
        id = 1234
        mock_db_session.query.side_effect = Exception()

        with pytest.raises(HTTPException):
            get_distributor_by_id(id, mock_db_session)


def test_get_distributor_lat_long_error_404(get_distributor):
    with patch('app.routes.distributor.get_db') as mock_db_session:
        lat, long = 10, 10
        (
            mock_db_session.query.return_value
            .filter.return_value
            .order_by.return_value
            .first.return_value
         ) = None

        with pytest.raises(HTTPException):
            get_distributor_by_lat_long(lat, long, mock_db_session)


def test_get_distributor_by_lat_long_error_500(get_distributor):
    with patch('app.routes.distributor.get_db') as mock_db_session:
        lat, long = 10, 10
        mock_db_session.query.side_effect = Exception()

        with pytest.raises(HTTPException):
            get_distributor_by_lat_long(lat, long, mock_db_session)


def test_post_distributor_error(get_distributor):
    with patch('app.routes.distributor.get_db') as mock_db_session:
        mock_db_session.commit.side_effect = Exception()

        distributor_request = DistributorBaseSchema(
            address=get_distributor['address'],
            coverage_area=get_distributor['coverage_area'],
            document=get_distributor['document'],
            owner_name=get_distributor['owner_name'],
            trading_name=get_distributor['trading_name'],
        )

        with pytest.raises(HTTPException):
            create_distributor(distributor_request, mock_db_session)
