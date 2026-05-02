from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession

from app.core.config.settings import settings


engine: AsyncEngine = create_async_engine(
    settings.URL_MYSQL,
    pool_size=10,             # Mantém até 10 conexões abertas
    max_overflow=20,          # Permite até 20 conexões extras em picos
    pool_recycle=3600,        # Recicla conexões a cada hora
    pool_pre_ping=True,       # Verifica se a conexão está viva antes de usar (evita erros 500)
)

SessionLocal: AsyncSession = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    autoflush=False,
    autocommit=False,
    expire_on_commit=False
)


async def get_session():
    async with SessionLocal() as session:
        yield session
