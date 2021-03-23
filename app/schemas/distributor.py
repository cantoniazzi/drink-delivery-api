from datetime import datetime
from enum import Enum
from typing import List
from typing import Optional

from pydantic import BaseModel


class MultipolygonType(Enum):
    MULTIPOLYGON = 'MultiPolygon'


class PointType(Enum):
    POINT = 'Point'


class AddressType(BaseModel):
    type: PointType
    coordinates: List[float]


class CoverageAreaType(BaseModel):
    type: MultipolygonType
    coordinates: List[List[List[List[float]]]]


class DistributorBaseSchema(BaseModel):
    address: AddressType
    coverage_area: CoverageAreaType
    document: str
    owner_name: str
    trading_name: str

    class Config:
        orm_mode = True


class DistributorResponseSchema(DistributorBaseSchema):
    id: int
    created_at: Optional[datetime]
    updated_at: Optional[datetime]

    class Config:
        orm_mode = True
