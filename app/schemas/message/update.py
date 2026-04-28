from pydantic import BaseModel

class UpdateMessageSchema(BaseModel):
    message_id: str
    content: str
