from pydantic import BaseModel, ConfigDict, field_validator

from app.core.constants import RoleEnum


class CreateMessageSchema(BaseModel):

    content: str 
    role: RoleEnum

    model_config = ConfigDict(from_attributes=True)
     

    @field_validator("role", mode="before")
    def validate_role(cls, value: str) -> RoleEnum:
        try:
            return RoleEnum(value)
        except Exception as exc:
            raise ValueError(f"Forneça corretamente o 'role': {str(exc)}") 