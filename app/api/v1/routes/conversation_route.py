from fastapi import APIRouter, status, HTTPException

from app.schemas.conversation import ConversationCreateSchema, ConversationReadSchema
from app.services import ConversationService

route = APIRouter()

@route.post("", status_code=status.HTTP_201_CREATED, response_model=ConversationReadSchema)
async def post_conversation(schema: ConversationCreateSchema) -> ConversationReadSchema: 
    try:
        conv_service = ConversationService()
        return await conv_service.create(schema)
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro do servidor externo: {str(exc)}"
        )

