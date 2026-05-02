from fastapi import APIRouter, status, HTTPException, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List

from app.schemas.conversation import (
    ConversationCreateSchema, 
    ConversationReadSchema, 
    ConversationUpdateSchema
)
from app.repositories import ConversationRepository
from app.core.config.deps import get_session
from app.exceptions import NotFoundError

route = APIRouter()

@route.post("", status_code=status.HTTP_201_CREATED, response_model=ConversationReadSchema)
async def post_conversation(schema: ConversationCreateSchema, session: AsyncSession = Depends(get_session)) -> ConversationReadSchema: 
    try:
        conv_repo = ConversationRepository(session=session)
        data = await conv_repo.create(schema.model_dump())
        await session.commit()
        return data
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro do servidor externo: {str(exc)}"
        )


@route.get("", status_code=status.HTTP_200_OK, response_model=List[ConversationReadSchema])
async def get_conversations(session: AsyncSession = Depends(get_session)):
    try:
        conv_repo = ConversationRepository(session=session)
        return await conv_repo.read_all()
    except Exception as exc:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Erro do servidor externo: {str(exc)}"
        )



@route.get("/{id}", status_code=status.HTTP_200_OK, response_model=ConversationReadSchema)
async def put_conversation(id: str, session: AsyncSession = Depends(get_session)):
    try:
        conv_repo = ConversationRepository(session=session)
        data = await conv_repo.read_by_id(id=id)

        if not data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Conversa não encontrada."
            )
            
        return data
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


@route.put("/{id}", status_code=status.HTTP_201_CREATED, response_model=ConversationReadSchema)
async def put_conversation(id: str, schema: ConversationUpdateSchema, session: AsyncSession = Depends(get_session)):
    try:
        conv_repo = ConversationRepository(session=session)
        data = await conv_repo.update(id=id, data=schema.model_dump())
        await session.commit()
        await session.refresh(data)
        return data
    
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

@route.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def delete_conversation(id: str, session: AsyncSession = Depends(get_session)):
    try:
        conv_repo = ConversationRepository(session=session)
        await conv_repo.delete(id=id)
        await session.commit()
        return 
    
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
