from app.models import ConversationModel
from app.core.config.deps import Session
from app.repositories.base_repository import BaseRepository

class ConversationRepository(BaseRepository):
    
    async def create(self, data: dict) -> ConversationModel:
        async with Session() as session:
            db_conv = ConversationModel(**data)
            session.add(db_conv)
            await session.commit()  

            session.refresh(db_conv)
        return db_conv
    
    
