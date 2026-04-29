import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


from app.main import app
from app.models.base_model import BaseModel


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine("sqlite:///database.db")
    BaseModel.registry.metadata.create_all(bind=engine)

    SessionLocal = sessionmaker(
        bind=engine
    )

    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()
    