from fastapi import FastAPI, Request, Depends, HTTPException, status,Form
from fastapi.responses import RedirectResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.staticfiles import StaticFiles
from db.db import engine
from models.model import Match
from dotenv import load_dotenv

import requests
import secrets
import os

from routers import matches

app = FastAPI()
security = HTTPBasic()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")




load_dotenv()





def get_current_username(credentials: HTTPBasicCredentials = Depends(security)):
    current_username_bytes = credentials.username
    correct_username_bytes = os.getenv("USUARIO")

    current_password_bytes = credentials.password
    correct_password_bytes = os.getenv("PASSWORD")

    is_correct_username = secrets.compare_digest(
        current_username_bytes, correct_username_bytes
    )
    is_correct_password = secrets.compare_digest(
        current_password_bytes, correct_password_bytes
    )
    if not (is_correct_password and is_correct_username):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect email or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return credentials.username



@app.get("/")
async def index(request: Request, username: str = Depends(get_current_username)):
    matches = await engine.find(Match)
    return templates.TemplateResponse(
        "registro.html", {"request": request, "matches": matches}
    )

@app.get("/login")
async def login(request: Request):

    return templates.TemplateResponse("login.html",{"request":request})

@app.get("/gastos")
async def index(request: Request):
    matches = await engine.find(Match)
    table_data = []
    for match in matches:
        table_data.append(match)
    return templates.TemplateResponse(
        "gastos.html",
        {"request": request, "matches": matches, "table_data": table_data},
    )


origins = ["http://localhost:8000", "http://127.0.0.1:8000"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(matches.router)
