from sqlalchemy import select


from app.models import ConversationModel


def test_create_conversation(session):
    conversation = ConversationModel(title="Oi")

    session.add(conversation)
    session.commit()

    assert conversation.title == "Oi"

    


