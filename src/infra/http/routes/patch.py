from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse
from fastapi import status

from src.__bs.request import ScrapSystem



patch = APIRouter(prefix="/newsletter")

@patch.patch("/newspappers/", tags=["newspapper"])
async def update_db():
    scrapper = ScrapSystem()
    scrapper.get_news()

    return JSONResponse(
        content=jsonable_encoder({"msg": "database updated, datas fetched"}),
        status_code=status.HTTP_200_OK
    )
