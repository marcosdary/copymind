from abc import ABC, abstractmethod
from typing import Any
class BaseRepository(ABC):
    
    @abstractmethod
    def create(self, data: Any): pass

    """ 
    @abstractmethod
    def read_all(self): pass


    @abstractmethod
    def read_by_id(self, id: str): pass


    @abstractmethod
    def update(self, id: str, data): pass


    @abstractmethod
    def delete(self, id: str): pass
    """
    


