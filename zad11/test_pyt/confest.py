import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from zad11.datbase.models import Base
from zad11.datbase.models import get_db
from fastapi import FastAPI
from main import main

SQLALCHEMY_DATABASE= "sqlite:///./test.db"
engine=create_engine(SQLALCHEMY_DATABASE, connect_args={"check_same_thread":False})

TestingSessionLocal= sessionmaker(autocommit=False, autoflush=False, bind=engie)

@pytest.fixture(scope="module")
def session():

    Base.metadata.drop_all(bind=engie)
    Base.metadata.create_all(bind=engie)

    db=TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()


@pytest.fixture(scope="module")
def client(session):
    app = FastAPI()
    def override_get_db():

        try:
            yield session
        finally:
            session.close()
    app.dependency_override[get_db]=override_get_db
    yield TestClient(app)

@pytest.fixture(scope="module")
def contact():
    return {first_name:"adam", last_name:"Kotel", date_of_birth:"2000-01-01"}


