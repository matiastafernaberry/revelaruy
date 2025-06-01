from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.scraper import scrape_news
from app.db import get_all_news

app = FastAPI()

# Montar archivos estáticos (CSS, JS)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    noticias = get_all_news()
    return templates.TemplateResponse("index.html", {"request": request, "noticias": noticias})

@app.get("/news")
def get_news():
    return get_all_news()

@app.post("/scrape")
def run_scraper():
    scrape_news()
    return {"status": "Scraping done"}
