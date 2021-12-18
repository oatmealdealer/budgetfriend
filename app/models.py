from datetime import datetime
from os import getenv
from typing import List, Optional

from pydantic import BaseModel, validator

import databases
import sqlalchemy

DATABASE_URL: str = getenv("DATABASE_URL")
database = databases.Database(DATABASE_URL)
metadata = sqlalchemy.MetaData()

users = sqlalchemy.Table(
    "users",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("created_at", sqlalchemy.DateTime, default=sqlalchemy.func.now()),
)

engine = sqlalchemy.create_engine(DATABASE_URL)
metadata.create_all(engine)


class UserInput(BaseModel):
    first_name: str
    last_name: str
    created_at: Optional[datetime]

    @validator("created_at")
    def remove_tzinfo(cls, timestamp: datetime):
        return timestamp.replace(tzinfo=None)


class User(BaseModel):
    id: int
    first_name: str
    last_name: str
    created_at: Optional[datetime]
