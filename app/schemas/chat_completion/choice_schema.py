from typing import Optional, Any
from pydantic import BaseModel
from app.schemas.chat_completion.chat_completion_message_schema import ChatCompletionMessageSchema

class ChoiceSchema(BaseModel):
    message: ChatCompletionMessageSchema

