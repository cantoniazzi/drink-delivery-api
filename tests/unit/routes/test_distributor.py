from unittest.mock import patch, Mock

from fastapi import HTTPException
import pytest

from app.routes.distributor import create_distributor
from app.schemas.distributor import DistributorBaseSchema


def test_post_distributor_error(get_distributor):
    with patch('app.routes.distributor.get_db') as mock_db_session:
        mock_db_session.add.side_effect = Exception()

        distributor_request = DistributorBaseSchema(
            address=get_distributor['address'],
            coverage_area=get_distributor['coverage_area'],
            document=get_distributor['document'],
            owner_name=get_distributor['owner_name'],
            trading_name=get_distributor['trading_name'],
        )

        with pytest.raises(HTTPException):
            create_distributor(distributor_request, mock_db_session)
