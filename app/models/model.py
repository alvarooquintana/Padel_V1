from odmantic import Field, Model, EmbeddedModel
from typing import Optional, Dict
from datetime import datetime


class User(Model):
    id: str = Field(primary_field=True)
    email: str
    password: str


class RegisterMatch(Model):
    id: str = Field(primary_field=True)
    water: float
    price: Dict[str, float]
    balls: float
    matches: float
    timestamp: Optional[datetime] = None
