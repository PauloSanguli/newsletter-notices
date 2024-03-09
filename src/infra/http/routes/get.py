from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status


get = APIRouter(prefix="/newsletter")

@get.get("/email/", tags=["email"])
def get_all_email():
    return JSONResponse(
        content=jsonable_encoder([]),
        status_code=status.HTTP_200_OK
    )

@get.get("/newspapper/", tags=["newspapper"])
def get_all_newspapper():
    return JSONResponse(
        content=jsonable_encoder([]),
        status_code=status.HTTP_200_OK
    )
    