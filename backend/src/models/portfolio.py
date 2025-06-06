from datetime import datetime



from sqlmodel import Field,  SQLModel




class Portfolio(SQLModel, table=True):
    id: int  = Field(primary_key=True)
    user: str = Field(nullable=False)
    name: str = Field(nullable=False)
    created_at: datetime = Field(nullable=False, default_factory=datetime.utcnow())
    updated_at: datetime = Field(nullable=True)
    deleted_at: datetime = Field(nullable=True)