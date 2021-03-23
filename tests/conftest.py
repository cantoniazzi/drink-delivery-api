from pytest import fixture

from app.common.db_connection import create_session
from app.common.settings import settings
from app.models.distributor import Distributor


@fixture()
def clear_database(request):
    filter_condition = request.param
    yield database_delete(request.param)
    database_delete(filter_condition)


def database_delete(filter_condition):
    session = create_session()
    register = session.query(Distributor).filter(*filter_condition)
    register.delete()
    session.commit()
    session.close()


@fixture()
def get_distributor():
    return {
        'address': {
            'type': 'Point',
            'coordinates': [10, 10]
        },
        'coverage_area': {
            'type': 'MultiPolygon',
            'coordinates': [[[[10, 10]]]]
        },
        'document': settings.get('distributor_document_fixture'),
        'owner_name': 'Integration Tester',
        'trading_name': 'Integration Tester Company'
    }
