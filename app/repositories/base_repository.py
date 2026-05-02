from abc import ABC, abstractmethod
from typing import Any

from sqlalchemy.ext.asyncio import AsyncSession
class BaseRepository(ABC):
    
    def __init__(self, session: AsyncSession):
        self.session = session
        super().__init__()

    @abstractmethod
    def create(self, data: Any): pass

    @abstractmethod
    def read_all(self): pass


    @abstractmethod
    def read_by_id(self, id: str): pass


    @abstractmethod
    def update(self, id: str, data): pass


    @abstractmethod
    def delete(self, id: str): pass
    
    


