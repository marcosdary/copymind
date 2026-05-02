from datetime import datetime
from sqlalchemy import select
from typing import List

from app.models import ConversationModel
from app.repositories.base_repository import BaseRepository
from app.exceptions import NotFoundError

class ConversationRepository(BaseRepository):
    
    async def create(self, data: dict) -> ConversationModel:
        db_conv = ConversationModel(**data)
        self.session.add(db_conv)
        await self.session.commit()  
        return db_conv
    
    
    async def read_all(self) -> List[ConversationModel]:
        return await self.session.scalars(select(ConversationModel))
    
    async def read_by_id(self, id: str):
        model = await self.session.scalar(
            select(ConversationModel).where(ConversationModel.conversationId == id)
        )

        if not model:
            raise NotFoundError("Recurso solicitado não é encontrado.")
        
        return model
    
     
    async def update(self, id: str, data: dict) -> ConversationModel: 
        model = await self.session.scalar(
            select(ConversationModel).where(ConversationModel.conversationId == id)
        )

        if not model:
            raise NotFoundError("Recurso solicitado não é encontrado.")

        for key, value in data.items():
            if value is not None:
                setattr(model, key, value)

        model.updatedAt = datetime.now()
        return model

    async def delete(self, id: str) -> None: 
        model = await self.session.scalar(
            select(ConversationModel).where(ConversationModel.conversationId == id)
        )
        if not model:
            raise NotFoundError("Recurso solicitado não é encontrado.")
        await self.session.delete(model)
