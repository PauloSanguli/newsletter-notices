"""main file"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.infra.http.routes.put import put
from src.infra.http.routes.get import get
from src.infra.http.routes.delete import delete

import uvicorn

from src.__bs.request import ScrapSystem
from src.notificate.sendEmail import Email



app = FastAPI(title="newsletter api")

app.include_router(put)
app.include_router(get)
app.include_router(delete)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)
if __name__=='__main__':
    """run the server with uvicorn"""
    # ScrapSystem().get_news()
    email_ = Email()
    email_.send()
    # uvicorn.run(
    #     app=app
    # )
