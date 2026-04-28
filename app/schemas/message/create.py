from pydantic import BaseModel, field_validator

from app.constants import RoleEnum


class CreateMessageSchema(BaseModel):

    content: str 
    role: RoleEnum

    class Config:
        from_attributes = True

    @field_validator("role", mode="before")
    def validate_role(cls, value: str) -> RoleEnum:
        try:
            return RoleEnum(value)
        except Exception as exc:
            raise ValueError(f"Forneça corretamente o 'role': {str(exc)}") 