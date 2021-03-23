from datetime import datetime
from json import loads
from typing import Any
from typing import List

from geoalchemy2 import Geometry
from geoalchemy2.functions import ST_AsGeoJSON
from geoalchemy2.functions import ST_Contains
from geoalchemy2.functions import ST_Distance
from geoalchemy2.functions import ST_GeomFromText
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

_SRID = 4326


def format_filter(point):
    return ST_Contains(Distributor.coverage_area, ST_GeomFromText(point, _SRID))


def get_query_fields() -> List[Any]:
    return [
        Distributor.id,
        Distributor.document,
        Distributor.owner_name,
        Distributor.trading_name,
        Distributor.created_at,
        Distributor.updated_at,
        ST_AsGeoJSON(Distributor.address).label('address'),
        ST_AsGeoJSON(Distributor.coverage_area).label('coverage_area'),
    ]


def format_order_by(point):
    return ST_Distance(Distributor.address, ST_GeomFromText(point, _SRID)).label(
        'distance'
    )


def parse_distributor(result):
    distributor = result._asdict()
    distributor['address'] = loads(distributor['address'])
    distributor['coverage_area'] = loads(distributor['coverage_area'])
    return distributor


class Distributor(Base):
    __tablename__ = 'distributor'

    id = Column(Integer, primary_key=True)
    address = Column(Geometry(geometry_type='POINT', srid=_SRID))
    created_at = Column(DateTime, default=datetime.now())
    coverage_area = Column(Geometry(geometry_type='MULTIPOLYGON', srid=_SRID))
    document = Column(String)
    owner_name = Column(String)
    trading_name = Column(String)
    updated_at = Column(DateTime, onupdate=datetime.now)

    @staticmethod
    def add(db_instance, distributor_request):
        distributor = Distributor(
            address=distributor_request.address.json(),
            coverage_area=distributor_request.coverage_area.json(),
            document=distributor_request.document,
            owner_name=distributor_request.owner_name,
            trading_name=distributor_request.trading_name,
        )
        db_instance.add(distributor)
        db_instance.commit()

        distributor.address = distributor_request.address
        distributor.coverage_area = distributor_request.coverage_area

        return distributor

    @staticmethod
    def get_by_id(db_instance, id: int):
        distributor = None

        result = db_instance.query(*get_query_fields()).filter(Distributor.id == id)
        if result and result.count():
            distributor = parse_distributor(result[0])

        return distributor

    @staticmethod
    def get_by_point(db_instance, lat, long):
        distributor = None
        point = f'POINT({lat} {long})'

        result = (
            db_instance.query(*get_query_fields())
            .filter(format_filter(point))
            .order_by(format_order_by(point))
            .first()
        )
        if result:
            distributor = parse_distributor(result)

        return distributor
