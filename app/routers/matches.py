from fastapi import APIRouter, Form, status
from fastapi.responses import RedirectResponse
from models.model import RegisterMatch,User
from utils.utils import get_hashed_password, verify_password,find_user_by_email
from databases.database import engine
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
    user = await find_user_by_email(email)
    if user:
        if not verify_password(plain_password, user.password):
            return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND) 
        else:
            return RedirectResponse(url="/registro", status_code=status.HTTP_302_FOUND)
    else:
        return RedirectResponse(url="/login", status_code=status.HTTP_302_FOUND) 


        


@router.get("/all_matches")
async def get_matches():
    matches = await engine.find(RegisterMatch)
    return matches


@router.post("/matches")
async def add_matches(
     balls: float = Form(), water: float = Form(), matches: float = Form()
):
    now = datetime.utcnow().strftime("%Y-%m-%d %H:%M")
    register_match = RegisterMatch(
        balls=balls,
        water=water,
        matches=matches,
        id=uuid.uuid4().hex,
        timestamp=now,
    )

    await engine.save(register_match)

    return RedirectResponse(url="/gastos", status_code=status.HTTP_302_FOUND)

@router.post("/results")
async def results():
    pass
