from datetime import datetime
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class PortfolioStock(SQLModel, table=True):
    id: int = Field(primary_key=True)
    portfolio_id: int = Field(nullable=False)
    stock_symbol: str = Field(nullable=False)
    purchase_value: float = Field(nullable=False)
    sell_value: float = Field(nullable=False)
    created_at: datetime = Field(nullable=False)
    updated_at: datetime = Field(nullable=True)
    deleted_at: datetime = Field(nullable=True)