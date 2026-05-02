from pydantic import BaseModel, ConfigDict

class ConversationUpdateSchema(BaseModel):
    
    title: str

    model_config = ConfigDict(from_attributes=True)