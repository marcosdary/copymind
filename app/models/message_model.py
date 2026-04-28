from decimal import Decimal

from sqlalchemy import BigInteger, Enum, ForeignKey, Numeric, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base_model import BaseModel

from app.constants import RoleEnum

class MessageModel(BaseModel):
    __tablename__ = "messages"

    message_id: Mapped[str] = mapped_column(String(255), primary_key=True)
    conversation_id: Mapped[str] = mapped_column(
        String(255),
        ForeignKey("conversations.conversation_id", ondelete="CASCADE"),
        nullable=False,
    )
    content: Mapped[str] = mapped_column(Text, nullable=False)
    total_tokens: Mapped[int] = mapped_column(BigInteger, nullable=False)
    total_response_time: Mapped[Decimal] = mapped_column(Numeric(12, 3), nullable=False)
    sent_by: Mapped[RoleEnum] = mapped_column(
        Enum(RoleEnum, name="roles", create_type=False),
        nullable=False,
    )

    conversation: Mapped["ConversationModel"] = relationship(back_populates="messages")
