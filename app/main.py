from fastapi import FastAPI,Request
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from db.db import engine
from models.model import Match

from routers import matches

app = FastAPI()

templates = Jinja2Templates(directory="templates")

origins = [
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



@app.get("/")
async def index(request: Request):
    matches = await engine.find(Match)
    return templates.TemplateResponse("index.html", {"request": request, "matches":matches})






app.include_router(matches.router)