from pydantic import BaseModel
from datetime import datetime


class RegisterMatches(BaseModel):
    water: float
    balls: float
    matches: float
    timestamp = datetime


class MatchesResponse(BaseModel):
    timestamp = datetime
    
