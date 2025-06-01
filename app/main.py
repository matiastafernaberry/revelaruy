from fastapi import FastAPI
from app.scraper import scrape_news
from app.db import get_all_news

app = FastAPI()

@app.get("/news")
def read_news():
    return get_all_news()

@app.post("/scrape")
def run_scraper():
    scrape_news()
    return {"status": "Scraping done"}
