from odmantic import Field, Model
from typing import Optional
from datetime import datetime


class Match(Model):
    id: str = Field(primary_field=True)
    water: int
    balls: int
    matches: int
    timestamp: Optional[datetime] = None
