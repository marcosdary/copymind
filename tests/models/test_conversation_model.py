from sqlalchemy import select
from dataclasses import asdict

from app.models import ConversationModel


def test_create_conversation(session):
    conversation = ConversationModel(title="Oi")

    session.add(conversation)
    session.commit()

    assert asdict(conversation) == {
        "conversationId": conversation.conversationId,
        "title": "Oi",
        "createdAt": conversation.createdAt,
        "updatedat": conversation.updatedAt
    }

    


