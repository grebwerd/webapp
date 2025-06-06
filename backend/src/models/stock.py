from datetime import datetime
from sqlmodel import Field, SQLModel


class Stock(SQLModel, table=True):
    stock_symbol: str  = Field(default=None, primary_key=True)
    current_value: float = Field(nullable=False)
    thirty_back_value: float = Field(nullable=False)
    sixty_back_value: float = Field(nullable=False)
    ninety_back_value: float = Field(nullable=False)
    created_at: datetime = Field(nullable=False, default_factory=datetime.utcnow)
    updated_at: datetime = Field(nullable=True)
    deleted_at: datetime = Field(nullable=True)

