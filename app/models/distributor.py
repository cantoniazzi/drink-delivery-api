from datetime import datetime

from geoalchemy2 import Geometry
from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


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
