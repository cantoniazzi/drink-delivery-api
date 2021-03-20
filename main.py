from uvicorn import run

from app.api import app as application


if __name__ == '__main__':
    run('main:application', host='0.0.0.0', port=5000, workers=4)
