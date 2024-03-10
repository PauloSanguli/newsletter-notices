from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status

from src.infra.repository import Repository




put = APIRouter(prefix="/newsletter", tags=["email"])

@put.put("/email/")
async def regist_email(email: str):
    response = Repository.insert_email(email)

    return JSONResponse(
        content=jsonable_encoder({"msg":response["msg"]}),
        status_code=response["status"],
    )