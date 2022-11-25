from fastapi import APIRouter, Form, status
from fastapi.responses import RedirectResponse
from models.model import Match, User
from utils.hashed_password import get_hashed_password, verify_password
from db.db import engine
from datetime import datetime
import uuid


router = APIRouter()


@router.post("/register")
async def register(email: str = Form(), password: str = Form()):
    hash_password = get_hashed_password(password)
    register_user = User(id=uuid.uuid4().hex, email=email, password=hash_password)
    await engine.save(register_user)
    return register_user


@router.post("/login")
async def login(email: str = Form(), plain_password: str = Form()):
    user = await engine.find(User)
    if user[0].email == email:
        if not verify_password(plain_password, user[0].password):
            return status.HTTP_404_NOT_FOUND
        else:
            return RedirectResponse(url="/", status_code=status.HTTP_302_FOUND)


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
