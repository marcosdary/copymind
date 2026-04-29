from decimal import Decimal
from datetime import datetime
from sqlalchemy import BigInteger, Enum, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel

from app.core.constants import RoleEnum

class MessageModel(BaseModel):
    __tablename__ = "messages"

    messageId: Mapped[str] = mapped_column(primary_key=True)
    conversationId: Mapped[str] = mapped_column(
        ForeignKey("conversations.conversationId", ondelete="CASCADE"),
        nullable=False,
    )
    content: Mapped[str] = mapped_column(nullable=False)
    totalTokens: Mapped[int] = mapped_column(nullable=False)
    totalResponseTime: Mapped[Decimal] = mapped_column(nullable=False)
    role: Mapped[RoleEnum] = mapped_column(nullable=False)

    conversation: Mapped["ConversationModel"] = relationship(back_populates="messages")
