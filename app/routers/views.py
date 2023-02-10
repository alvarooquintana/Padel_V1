from fastapi import FastAPI, Request,status
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from databases.database import engine
from models.model import Match


app = FastAPI()

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


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

