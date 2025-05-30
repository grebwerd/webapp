from datetime import datetime
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Stock(SQLModel, table=True):
    stock_symbol: str  = Field(default=None, primary_key=True)
    current_value: float = Field(nullable=False)
    thirty_back_value: float = Field(nullable=False)
    sixty_back_value: float = Field(nullable=False)
    ninety_back_value: float = Field(nullable=False)
    created_at: datetime = Field(nullable=False)
    updated_at: datetime = Field(nullable=True)
    deleted_at: datetime = Field(nullable=True)

