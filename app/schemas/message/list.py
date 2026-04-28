from pydantic import BaseModel, field_serializer, RootModel
from typing import List

from app.schemas.message.create import CreateMessageSchema


class ListMessageSchema(RootModel[List[CreateMessageSchema]]):
    pass