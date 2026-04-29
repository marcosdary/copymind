from pydantic import BaseModel, ConfigDict

from app.core.constants import ModelIAEnum
from app.schemas.message.list import ListMessageSchema

class CompletionSchema(BaseModel):

    messages: ListMessageSchema
    model: ModelIAEnum 

    model_config = ConfigDict(from_attributes=True)
