from typing import Annotated, Sequence, Dict

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Session, SQLModel, create_engine, select

from backend.src.models.portfolio import Portfolio



sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def get_session():
    with Session(engine) as session:
        yield session


SessionDep = Annotated[Session, Depends(get_session)]

app = FastAPI()


@app.on_event("startup")
def on_startup():
    create_db_and_tables()

@app.post("/portfolios/")
def create_portfolio(portfolio: Portfolio, session: SessionDep) -> Portfolio:
    session.add(portfolio)
    session.commit()
    session.refresh(portfolio)
    return portfolio


@app.get("/portfolios/")
def read_portfolios(
    session: SessionDep,
    offset: int = 0,
    limit: Annotated[int, Query(le=100)] = 100,
) -> Sequence[Portfolio]:
    portfolios = session.exec(select(Portfolio).offset(offset).limit(limit)).all()
    return portfolios


@app.get("/portfolios/{portfolio_id}")
def read_portfolio(portfolio_id: int, session: SessionDep) -> Portfolio:
    portfolio = session.get(Portfolio, portfolio_id)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Hero not found")
    return portfolio


@app.delete("/portfolios/{portfolio_id}")
def delete_portfolio(portfolio_id: int, session: SessionDep) -> dict[str, bool]:
    portfolio = session.get(Portfolio, portfolio_id)
    if not portfolio:
        raise HTTPException(status_code=404, detail="Hero not found")
    session.delete(portfolio)
    session.commit()
    return {"ok": True}
