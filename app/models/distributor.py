from datetime import datetime
from json import loads
from typing import Any
from typing import List

from geoalchemy2 import Geometry
from geoalchemy2.functions import ST_AsGeoJSON
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def get_query_fields() -> List[Any]:
    return [
          Distributor.id,
          Distributor.document,
          Distributor.owner_name,
          Distributor.trading_name,
          Distributor.created_at,
          Distributor.updated_at,
          ST_AsGeoJSON(Distributor.address).label('address'),
          ST_AsGeoJSON(Distributor.coverage_area).label('coverage_area')
    ]


class Distributor(Base):
    __tablename__ = 'distributor'

    id = Column(Integer, primary_key=True)
    address = Column(Geometry('POINT', srid=4326))
    created_at = Column(DateTime, default=datetime.now())
    coverage_area = Column(Geometry('MULTIPOLYGON'))
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
            distributor = result[0]._asdict()
            distributor['address'] = loads(distributor['address'])
            distributor['coverage_area'] = loads(distributor['coverage_area'])
        return distributor
