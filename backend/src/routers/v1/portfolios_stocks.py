from typing import Annotated, Sequence

from fastapi import APIRouter, Query, HTTPException
from sqlmodel import select

from backend.src.dependencies import SessionDep
from backend.src.models.portfolio_stock import PortfolioStock


router = APIRouter()
BASE_PATH = "/v1/portfolios_stocks"
PORTFOLIO_STOCK_ID = "{portfolio_stock_id}"

@router.post(BASE_PATH)
def create_portfolios_stocks(portfolio_stock: PortfolioStock, session: SessionDep) -> PortfolioStock:
    session.add(portfolio_stock)
    session.commit()
    session.refresh(portfolio_stock)
    return portfolio_stock


@router.get(BASE_PATH)
def read_portfolios_stocks(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> Sequence[PortfolioStock]:
    portfolios_stocks = session.exec(select(PortfolioStock).offset(offset).limit(limit)).all()
    return portfolios_stocks


@router.get(BASE_PATH + "/" + PORTFOLIO_STOCK_ID)
def read_portfolio_stock(portfolio_stock_id: int, session: SessionDep) -> PortfolioStock:
    portfolio_stock = session.get(PortfolioStock, portfolio_stock_id)
    if not portfolio_stock:
        raise HTTPException(status_code=404, detail="PortfolioStock not found")
    return portfolio_stock

@router.delete(BASE_PATH + "/" + PORTFOLIO_STOCK_ID)
def delete_portfolio_stock(portfolio_stock_id: int, session: SessionDep) -> dict[str, bool]:
    portfolio_stock = session.get(PortfolioStock, portfolio_stock_id)
    if not portfolio_stock:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    session.delete(portfolio_stock)
    session.commit()
    return {"ok": True}