from odmantic import Field, Model
from typing import Optional
from datetime import datetime


class Match(Model):
    id: str = Field(primary_field=True)
    water: float
    balls: float
    matches: float
    timestamp: Optional[datetime] = None


class User(Model):
    id: str = Field(primary_field=True)
    email: str
    password: str
