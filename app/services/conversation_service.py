from app.schemas.conversation import ConversationCreateSchema, ConversationReadSchema
from app.repositories import ConversationRepository
class ConversationService:

    def __init__(self):
        self.repo = ConversationRepository()

    def create(self, schema: ConversationCreateSchema) -> ConversationReadSchema:
        user = self.repo.create(schema.model_dump())
        return user 

