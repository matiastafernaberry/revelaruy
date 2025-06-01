import requests
from bs4 import BeautifulSoup
from app.db import save_news

def scrape_news():
    res = requests.get("https://www.elpais.com.uy/")
    soup = BeautifulSoup(res.text, "html.parser")
    headlines = soup.select("h2")

    for h in headlines[:5]:
        title = h.text.strip()
        link = h.find("a")["href"] if h.find("a") else ""
        save_news(title, link)
