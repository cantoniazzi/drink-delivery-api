from uvicorn import run

from app.api import app as application
from app.common.log import create_logger


if __name__ == '__main__':
    create_logger()
    run('main:application', host='0.0.0.0', port=5000, workers=4)
