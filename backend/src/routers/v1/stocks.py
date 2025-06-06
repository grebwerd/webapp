from typing import Annotated, Sequence

from fastapi import APIRouter, Query, HTTPException
from sqlmodel import select

from backend.src.dependencies import SessionDep
from backend.src.models.stock import Stock

router = APIRouter()
BASE_PATH = "/v1/stocks"
STOCK_SYMBOL = "{stock_symbol}"

@router.post(BASE_PATH)
def create_stock(stock: Stock, session: SessionDep) -> Stock:
    session.add(stock)
    session.commit()
    session.refresh(stock)
    return stock

@router.get(BASE_PATH)
def read_portfolios(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> Sequence[Stock]:
    portfolios = session.exec(select(Stock).offset(offset).limit(limit)).all()
    return portfolios


@router.get(BASE_PATH + "/" + STOCK_SYMBOL)
def read_portfolio(stock_symbol: str, session: SessionDep) -> Stock:
    portfolio = session.get(Stock, stock_symbol)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Stock not found")
    return portfolio


@router.delete(BASE_PATH + "/" + STOCK_SYMBOL)
def delete_portfolio(stock_symbol: str, session: SessionDep) -> dict[str, bool]:
    portfolio = session.get(Stock, stock_symbol)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Stock not found")
    session.delete(portfolio)
    session.commit()
    return {"ok": True}