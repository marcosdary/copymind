import pytest
from datetime import datetime
from contextlib import contextmanager
from fastapi.testclient import TestClient
from sqlalchemy import create_engine, event
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

@contextmanager
def _moke_db_time(*, model, time=datetime(2026, 1, 1)):
    def fake_time_mock(mapper, connection, target):
        if hasattr(target, 'createdAt'):
            target.createdAt = time
    
    event.listen(model, 'before_insert', fake_time_mock)

    yield time

    event.remove(model, "before_insert", fake_time_mock)

    
@pytest.fixture
def mock_db_time():
    return _moke_db_time
