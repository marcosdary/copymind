from fastapi import APIRouter, status, HTTPException

from app.schemas import CompletionSchema
from app.schemas.chat_completion import ChatCompletionSchema

route = APIRouter()

@route.post("", status_code=status.HTTP_201_CREATED)
async def post_message(schema: CompletionSchema) -> ChatCompletionSchema: 
    from app.services import GroqService
    try:
        groq_service = GroqService()
        chat_completion = await groq_service.chat_completion(**schema.model_dump())
        return chat_completion
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro do servidor externo: {str(exc)}"
        )