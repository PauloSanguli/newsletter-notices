from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status


put = APIRouter(prefix="/newsletter", tags=["email"])

@put.put("/email/")
async def regist_email(email: str):
    return JSONResponse(
        content=jsonable_encoder({
            "msg": "email registed!"
        }),
        status_code=status.HTTP_201_CREATED,
    )