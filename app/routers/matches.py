from fastapi import APIRouter, Form, status
from fastapi.responses import RedirectResponse
from models.model import Match, User
from utils.hashed_password import get_hashed_password
from db.db import engine
from datetime import datetime
import uuid


router = APIRouter()


@router.post("/register")
async def register(email: str = Form(), password: str = Form()):
    hash_password = get_hashed_password(password)
    register_user = User(id=uuid.uuid4().hex,email=email, password=hash_password)
    await engine.save(register_user)
    return register_user


@router.get("/all_matches")
async def get_matches():
    matches = await engine.find(Match)
    return matches


@router.post("/matches")
async def add_matches(
    balls: float = Form(), water: float = Form(), matches: float = Form()
):
    register_matches = Match(
        balls=balls,
        water=water,
        matches=matches,
        id=uuid.uuid4().hex,
        timestamp=datetime.utcnow(),
    )

    await engine.save(register_matches)

    return RedirectResponse(url="/gastos", status_code=status.HTTP_302_FOUND)
