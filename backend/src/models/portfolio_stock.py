from datetime import datetime
from typing import Optional

from sqlmodel import Field, SQLModel


class PortfolioStock(SQLModel, table=True):
    id: int = Field(primary_key=True)
    portfolio_id: int = Field(nullable=False)
    stock_symbol: str = Field(nullable=False)
    purchase_value: float = Field(nullable=False)
    sell_value: float = Field(default=-1, nullable=False)
    created_at: datetime = Field(nullable=False, default_factory=datetime.utcnow)
    updated_at: datetime = Field(nullable=True)
    deleted_at: datetime = Field(nullable=True)