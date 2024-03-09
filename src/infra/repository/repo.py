from src.application.repository import IRepository



class Repository(IRepository):
    """repository for all models"""
    def insert_email(email: str) -> dict:
        """regist email"""
        return super().insert_email()
    
    def get_all_email() -> list:
        """select all emails from db"""

    def get_all_newspapper() -> list:
        """select all newspapper from db"""
