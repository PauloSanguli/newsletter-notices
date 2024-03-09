from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.infra.http.routes.put import put
from src.infra.http.routes.get import get

app = FastAPI(title="newsletter api")

app.include_router(put)
app.include_router(get)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)
