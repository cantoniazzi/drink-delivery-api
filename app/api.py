from fastapi import FastAPI


app = FastAPI(
   title='Drink Delivery API',
   description='A centralized service to managing beverage distributors.',
)


@app.get('/')
@app.get('/healthcheck')
async def health_check():
    return {'message': 'Drink delivery api it is running like a charm'}
