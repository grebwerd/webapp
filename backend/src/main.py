from fastapi import FastAPI
from backend.src.dependencies import  create_db_and_tables
from backend.src.routers.v1 import portfolios, stocks, portfolios_stocks

app = FastAPI()
app.include_router(portfolios.router, tags=["portfolios"])
app.include_router(stocks.router, tags=["stocks"])
app.include_router(portfolios_stocks.router, tags=["portfolio_stocks"])


@app.on_event("startup")
def on_startup():
    create_db_and_tables()
