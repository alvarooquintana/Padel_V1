from pydantic import BaseModel
from datetime import datetime


class RegisterMatches(BaseModel):
    water: int
    balls: int
    matches: int
    timestamp = datetime


class MatchesResponse(BaseModel):
    timestamp = datetime
    
