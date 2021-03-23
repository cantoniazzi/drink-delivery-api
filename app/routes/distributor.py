from logging import getLogger

from fastapi import APIRouter
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Query
from fastapi import status
from sqlalchemy.orm import Session

from app.common.db_connection import get_db
from app.models.distributor import Distributor
from app.schemas.distributor import DistributorBaseSchema
from app.schemas.distributor import DistributorResponseSchema


logger = getLogger()
router = APIRouter()


@router.post('/', response_model=DistributorResponseSchema, status_code=status.HTTP_201_CREATED)
def create_distributor(distributor_request: DistributorBaseSchema, db_instance: Session = Depends(get_db)):
    try:
        return Distributor.add(db_instance, distributor_request)
    except Exception as error:
        logger.error(
            f'Error when trying to create distributor {str(error)}',
            extra={'_body': str(distributor_request), '_error': str(error)}
        )
        raise HTTPException(status_code=500)


@router.get('/{id}', response_model=DistributorResponseSchema)
def get_distributor_by_id(id: int, db_instance: Session = Depends(get_db)):
    distributor = None
    try:
        distributor = Distributor.get_by_id(db_instance, id)
    except Exception as error:
        logger.error(
            f'Error when trying to get distributor by id {str(error)}',
            extra={'_distributor_id': id, '_error': str(error)}
        )
        raise HTTPException(status_code=500)

    if not distributor:
        raise HTTPException(status_code=404)

    return distributor


@router.get('/', response_model=DistributorResponseSchema)
def get_distributor_by_lat_long(
    lat: float = Query(..., le=90, ge=-90),
    long: float = Query(..., le=180, ge=-180),
    db_instance: Session = Depends(get_db)
):
    distributor = None
    try:
        distributor = Distributor.get_by_point(db_instance, lat, long)
    except Exception as error:
        logger.error(
            f'Error when trying to get distributor by lat long {str(error)}',
            extra={
                '_distributor_id': id,
                '_error': str(error),
                '_lat': lat,
                '_long': long
            }
        )
        raise HTTPException(status_code=500)

    if not distributor:
        raise HTTPException(status_code=404)

    return distributor
