from fastapi import APIRouter,Form, status
from fastapi.responses import RedirectResponse
from models.model import Match
from db.db import engine
from datetime import datetime
import uuid


router = APIRouter()


@router.get("/all_matches")
async def get_matches():
    matches = await engine.find(Match)
    return matches


@router.post("/matches")
async def add_matches(balls: float = Form(),water:float = Form(),matches:float = Form()):
    register_matches = Match(
        balls=balls,
        water=water,
        matches=matches,
        id=uuid.uuid4().hex,
        timestamp=datetime.utcnow(),
    )

    await engine.save(register_matches)

    return RedirectResponse(url="/gastos", status_code=status.HTTP_302_FOUND)
