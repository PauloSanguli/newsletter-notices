from sqlalchemy.orm import Session
from sqlalchemy import delete
from src.infra.models import engine, emails, newspapper

from fastapi import status

class Controller:
    """controller for all models"""
    def delete_email(email: str) -> bool:
        """delete email"""
        with Session(engine) as session:
            session.execute(delete(emails).\
                where(emails.c.email==email))
            session.commit()
    
    def delete_all_newspapper() -> bool:
        """delete all newspapper for update"""
        with Session(engine) as session:
            session.execute(newspapper.delete())
            session.commit()

    def update_newspapper(_newspapper: list) -> bool:
        """update newspapper"""
        with Session(engine) as session:
            session.execute(newspapper.insert(), _newspapper)   
            session.commit()
        