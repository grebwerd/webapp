from datetime import datetime
from typing import Annotated

from fastapi import Depends, FastAPI, HTTPException, Query
from sqlmodel import Field, Session, SQLModel, create_engine, select


class Portfolio(SQLModel, table=True):
    id: int  = Field(primary_key=True)
    user: str = Field(nullable=False)
    name: str = Field(nullable=False)
    created_at: datetime = Field(nullable=False)
    updated_at: datetime = Field(nullable=True)
    deleted_at: datetime = Field(nullable=True)
