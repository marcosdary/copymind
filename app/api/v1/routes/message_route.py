from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.core.config.deps import get_session
from app.schemas import CompletionSchema
from app.schemas.conversation import ConversationReadSchema
from app.services import GroqService
from app.tools import execute_tool
from app.exceptions import NotFoundError

route = APIRouter()

@route.post("", status_code=status.HTTP_201_CREATED, response_model=List[ConversationReadSchema])
async def post_message(schema: CompletionSchema, session: AsyncSession = Depends(get_session)) -> List[ConversationReadSchema]: 
    try:
        groq_service = GroqService()

        chat_completion = await groq_service.chat_completion(model=schema.model, messages=schema.messages.model_dump())

        tool_calls = chat_completion.choices[0].message.tool_calls
        
        return await execute_tool(tool_calls, session)
    
    except NotFoundError as exc:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(exc)
        )
    
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro do servidor externo: {str(exc)}"
        )

