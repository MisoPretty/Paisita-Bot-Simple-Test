
from fastapi import FastAPI,Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn

app=FastAPI()

app.mount("/static",StaticFiles(directory="dashboard/static"),name="static")
templates=Jinja2Templates(directory="dashboard/templates")

@app.get("/")
async def index(request:Request):

    dummy_stats={
        "equity":10000.0,
        "daily_pnl":0.0,
        "open_risk":0.0,
        "open_positions":[],
        "candidate_trades":[],
    }

    return templates.TemplateResponse(
        "index.html",
        {"request":request,"stats":dummy_stats},
    )

def run_dashboard(config:dict):
    uvicorn.run("dashboard.app:app",
        host=config["dashboard"]["host"],
        port=int(config["dashboard"]["port"]),
        reload=True
    )
