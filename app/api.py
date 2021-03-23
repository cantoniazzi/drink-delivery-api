from fastapi import FastAPI
from starlette_prometheus import metrics
from starlette_prometheus import PrometheusMiddleware

from app.routes import distributor


app = FastAPI(
   title='Drink Delivery API',
   description='A centralized service to managing beverage distributors.',
)
app.add_middleware(PrometheusMiddleware)
app.add_route('/metrics', metrics)


@app.get('/healthcheck')
async def health_check():
    return {'message': 'Drink delivery api it is running like a charm'}


app.include_router(
   distributor.router,
   prefix='/distributor',
   tags=['distributor']
)
