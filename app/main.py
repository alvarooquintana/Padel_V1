from fastapi import FastAPI, Request, Depends, HTTPException, status, Form
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



@app.get("/")
async def index():
    return RedirectResponse(url="login", status_code=status.HTTP_302_FOUND)

@app.get("/registro")
async def index(request: Request):
    matches = await engine.find(Match)
    return templates.TemplateResponse(
        "registro.html", {"request": request, "matches": matches}
    )


@app.get("/login")
async def login(request: Request):

    return templates.TemplateResponse("login.html", {"request": request})


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
