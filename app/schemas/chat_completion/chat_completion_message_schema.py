from pydantic import BaseModel
from typing import Optional
from app.schemas.chat_completion.structured_output_schema import StructuredOutputSchema

class ChatCompletionMessageSchema(BaseModel):
    content: str
    role: str
    structured_output: Optional[StructuredOutputSchema] = None
    reasoning: Optional[str] = None
