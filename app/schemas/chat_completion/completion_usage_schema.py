from pydantic import BaseModel
from typing import Optional

class CompletionUsageSchema(BaseModel):
    completion_tokens: int
    prompt_tokens: int
    total_tokens: int
    completion_time: Optional[float] = 0.0
    prompt_time: Optional[float] = 0.0
    queue_time: Optional[float] = 0.0
    total_time: Optional[float] = 0.0

