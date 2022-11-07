from fastapi import APIRouter,Request
from schemas.schema import RegisterMatches, MatchesResponse
from models.model import Match
from db.db import engine
from datetime import datetime
from fastapi.templating import Jinja2Templates
import uuid


router = APIRouter()


@router.get("/matches")
async def get_matches():
    matches = await engine.find(Match)
    return matches    


@router.post("/matches", response_model=MatchesResponse)
async def add_matches(create_match: RegisterMatches):
    register_matches = Match(
        balls=create_match.balls,
        water=create_match.water,
        matches=create_match.matches,
        id=uuid.uuid4().hex,
        timestamp=datetime.utcnow(),
    )

    await engine.save(register_matches)
    return register_matches

 

