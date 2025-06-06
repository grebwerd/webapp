from fastapi import FastAPI
from backend.src.dependencies import  create_db_and_tables
from backend.src.routers.v1 import portfolio

app = FastAPI()
app.include_router(portfolio.router, tags=["portfolio"])


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
