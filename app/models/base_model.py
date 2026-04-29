from datetime import datetime

from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class BaseModel(DeclarativeBase):
    __abstract__ = True

    createdAt: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now)
    updatedAt: Mapped[datetime] = mapped_column(nullable=False, default=datetime.now)
