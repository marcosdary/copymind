from fastapi import APIRouter, status, HTTPException

from app.schemas.message import ListMessageSchema
from app.schemas.chat_completion import ChatCompletionSchema

router = APIRouter(prefix="/v1/message")

@router.post("", status_code=status.HTTP_201_CREATED)
async def post_message(schema: ListMessageSchema) -> ChatCompletionSchema: 
    from app.services import LlamaVersatileAIService, GptOssAIService

    try:
        model_ai_service = GptOssAIService()
        chat_completion = await model_ai_service.chat_completion(schema.model_dump())
        return chat_completion
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro do servidor externo: {str(exc)}"
        )