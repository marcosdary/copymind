from pydantic import BaseModel, ConfigDict
from datetime import datetime

class ConversationReadSchema(BaseModel):
    
    conversationId: str
    title: str
    createdAt: datetime
    updatedAt: datetime

    model_config = ConfigDict(from_attributes=True)