from pydantic import BaseModel, Field

from app.core.constants import ToneEnum, LanguageEnum

class StructuredOutputSchema(BaseModel):
    answer: list[str] = Field(min_length=1)
    tone: ToneEnum
    language: LanguageEnum
    confidence: float = Field(ge=0.0, le=1.0)
    next_actions: list[str] = Field(default_factory=list)
