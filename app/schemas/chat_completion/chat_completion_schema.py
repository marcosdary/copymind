from typing import List, Optional
from pydantic import BaseModel
from app.schemas.chat_completion.choice_schema import ChoiceSchema
from app.schemas.chat_completion.completion_usage_schema import CompletionUsageSchema

class ChatCompletionSchema(BaseModel):
    id: str
    choices: List[ChoiceSchema]
    model: str
    usage: CompletionUsageSchema
    file_url: Optional[str] = None
   