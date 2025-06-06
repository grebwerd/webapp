from fastapi import FastAPI
from backend.src.dependencies import  create_db_and_tables
from backend.src.routers.v1 import portfolios, stocks

app = FastAPI()
app.include_router(portfolios.router, tags=["portfolio"])
app.include_router(stocks.router, tags=["stock"])


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
