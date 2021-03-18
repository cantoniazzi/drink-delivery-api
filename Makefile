APP_NAME="drink-delivery-api"

### docker commands
docker/build:
		docker-compose build ${APP_NAME}

docker/run:
		docker-compose run --service-port ${APP_NAME} python main.py

docker/test:
		docker-compose run ${APP_NAME} \
		python -m pytest -s --pyargs ./tests ./app

### local commands
local/install:
		pipenv install --dev

local/lint:
		flake8 src/

local/run:
		python main.py

local/test:
		python -m pytest ./app --pyargs ./tests
