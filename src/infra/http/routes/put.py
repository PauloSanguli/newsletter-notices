from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status

from src.infra.repository import Repository

from src.notificate.sendEmail import Email




put = APIRouter(prefix="/newsletter")

@put.put("/email/", tags=["email"])
async def regist_email(email: str):
    response = Repository.insert_email(email)

    return JSONResponse(
        content=jsonable_encoder({"msg":response["msg"]}),
        status_code=response["status"],
    )

@put.put("/send/", tags=["newspapper"])
async def send_email():
    emailInstance = Email()
    response = emailInstance.send()

    if response["status"]:
        return JSONResponse(
            content=jsonable_encoder({
                "error": f"{response['error']}",
                "msg": "email not sended"
            }),
            status_code=response["status"]
        )
    return JSONResponse(
        content=jsonable_encoder({
            "msg": f"{response['msg']}"
        }),
        status_code=status.HTTP_200_OK
    )
