# drink-delivery-api

[![Python 3.8.3](https://img.shields.io/badge/python-3.8.3-blue.svg)](https://www.python.org/downloads/release/python-383/) [![main](https://github.com/cantoniazzi/drink-delivery-api/actions/workflows/main.yml/badge.svg)](https://github.com/cantoniazzi/drink-delivery-api/actions/workflows/main.yml)

It's responsible for managing the registration flow of beverage distributors.

## architecture

![drink-delivery-api](docs/drink-delivery-api.png)

## built With

- [Python 3.8.3](https://www.python.org/downloads/release/python-383/)
- [Pipenv](https://github.com/pypa/pipenv)
- [FastAPI](https://github.com/tiangolo/fastapi)
- [Uvicorn](https://github.com/encode/uvicorn)
- [Sql Alchemy](https://www.sqlalchemy.org/)
- [GeoAlchemy2](https://geoalchemy-2.readthedocs.io/en/latest/)
- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/)

## monitoring

- [X] - [Sentry](https://sentry.io/organizations/cassiosvaldo/issues/?project=5685277)

We have also configured the `/ metrics` route that exports metrics for [prometheus](https://prometheus.io/).

### How to build

```sh
make docker/build
```

## how to run

```sh
make docker/run
```

## how to lint

```sh
make docker/lint
```

## how to test

```sh
make docker/test-unit
make docker/test-integration
```

We separate a specific [document](`https://github.com/cantoniazzi/drink-delivery-api/blob/main/settings.toml#L10`) to be used in the integrations tests in a parameterized way. You can change this number in the configuration if you wish.

## how to deploy

in soon.

## miscellanies

To update the project diagram initilize your local environment:

```sh
make local/init
```

So run the command:

```sh
make local/diagram
```
