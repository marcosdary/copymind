from pydantic import BaseModel, ConfigDict

class ConversationCreateSchema(BaseModel):
    
    title: str

    model_config = ConfigDict(from_attributes=True)