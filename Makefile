APP_NAME="drink-delivery-api"

### docker commands
docker/build:
		docker-compose build ${APP_NAME}

docker/lint:
		docker-compose run ${APP_NAME} flake8 app/

docker/run:
		docker-compose run --service-port ${APP_NAME} python main.py

docker/test-integration:
		docker-compose run -e ENV_FOR_DYNACONF=test ${APP_NAME} \
		python -m pytest -s --pyargs ./tests/integration -s ./app

docker/test-unit:
		docker-compose run -e ENV_FOR_DYNACONF=test ${APP_NAME} \
		python -m pytest -s --pyargs ./tests/unit -s ./app


### local commands
local/install:
		pipenv install --dev

local/lint:
		flake8 app/

local/run:
		python main.py

local/test:
		python -m pytest ./app --pyargs ./tests