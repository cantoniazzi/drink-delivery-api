from os import getenv as env

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def create_session():
    engine = create_engine(get_connection_string())
    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    return Session()


def get_connection_string():
    driver = 'postgresql+psycopg2'
    return f"{driver}://{env('PG_USER')}:{env('PG_PASSWORD')}@{env('PG_HOST')}:{env('PG_PORT')}/{env('PG_DB')}"


def get_db():
    try:
        db = create_session()
        yield db
    finally:
        if db:
            db.close()
