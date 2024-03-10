from src.application.repository import IRepository

from sqlalchemy.orm import Session
from src.infra.models import engine, emails, newspapper

from src.validator import email as SchemaEmail

from cerberus import Validator

from fastapi import status

from sqlalchemy.exc import IntegrityError


class Repository(IRepository):
    """repository for all models"""
    __validator = Validator()

    def insert_email(email: str) -> dict:
        """regist email"""
        __result = Repository.__validator.validate(
            {"email": email},
            SchemaEmail
        )

        if __result:
            try:
                with Session(engine) as session:
                    session.execute(emails.insert(), {"email": email})
                    session.commit()
            except IntegrityError:
                __msg = "email alredy exists"
                status_code = status.HTTP_400_BAD_REQUEST
            else:
                __msg = "email inerted with sucess"
                status_code = status.HTTP_201_CREATED
        else:
            __msg = "invalid format of email"
            status_code = status.HTTP_400_BAD_REQUEST
        return {
            "msg": __msg,
            "status": status_code
        }
        
    def get_all_email() -> list:
        """select all emails from db"""
        with Session(engine) as session:
            datas = session.execute(emails.select()).fetchall()

    def get_all_newspapper() -> list:
        """select all newspapper from db"""
        with Session(engine) as session:
            datas = session.execute(newspapper.select()).fetchall()
