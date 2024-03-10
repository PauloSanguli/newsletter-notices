from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status

from src.infra.http.controllers import Controller


delete = APIRouter(prefix="/email", tags=["email"])

@delete.delete("/email/")
async def delete_email(email: str):
    Controller.delete_email(email)

    return JSONResponse(
        content=jsonable_encoder({
            "msg": "email deleted"
        }),
        status_code=status.HTTP_200_OK
    )

