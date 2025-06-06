from typing import Annotated, Sequence

from fastapi import APIRouter, Query, HTTPException
from sqlmodel import select

from backend.src.dependencies import SessionDep
from backend.src.models.portfolio import Portfolio

router = APIRouter()
BASE_PATH = "/v1/portfolios"
PORTFOLIO_ID = "{portfolio_id}"

@router.post(BASE_PATH)
def create_portfolio(portfolio: Portfolio, session: SessionDep) -> Portfolio:
    session.add(portfolio)
    session.commit()
    session.refresh(portfolio)
    return portfolio


@router.get(BASE_PATH)
def read_portfolios(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> Sequence[Portfolio]:
    portfolios = session.exec(select(Portfolio).offset(offset).limit(limit)).all()
    return portfolios


@router.get(BASE_PATH + "/" + PORTFOLIO_ID)
def read_portfolio(portfolio_id: int, session: SessionDep) -> Portfolio:
    portfolio = session.get(Portfolio, portfolio_id)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    return portfolio


@router.delete(BASE_PATH + "/" + PORTFOLIO_ID)
def delete_portfolio(portfolio_id: int, session: SessionDep) -> dict[str, bool]:
    portfolio = session.get(Portfolio, portfolio_id)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Portfolio not found")
    session.delete(portfolio)
    session.commit()
    return {"ok": True}