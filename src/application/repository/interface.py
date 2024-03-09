"""Interface for repositorys"""
from abc import ABC, abstractmethod



class IRepository(ABC):
    @abstractmethod
    def insert_email(email: str) -> dict:
        raise NotImplementedError("method insert_email required!")
    
    @abstractmethod
    def get_all_email() -> list:
        raise NotImplementedError("method get_all_email required!")
    
    @abstractmethod
    def get_all_newspapper() -> list:
        raise NotImplementedError("method get_all_newspapper required!")
