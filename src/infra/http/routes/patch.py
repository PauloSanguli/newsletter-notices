from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status

from src.__bs.request import ScrapSystem



patch = APIRouter(prefix="/newsletter")

@patch.patch("/newspappers/", tags=["newspapper"])
async def update_db():
    scrapper = ScrapSystem()
    msg, __status = scrapper.get_news()

    if __status:
        return JSONResponse(
            content=jsonable_encoder({"msg": "database updated, datas fetched"}),
            status_code=status.HTTP_200_OK
        )
    return JSONResponse(
        content=jsonable_encoder({
            "msg": f"{msg}"
        }),
        status_code=status.HTTP_408_REQUEST_TIMEOUT
    )
