import sqlite3
from datetime import datetime

conn = sqlite3.connect("news.db", check_same_thread=False)
cur = conn.cursor()
cur.execute('''
    CREATE TABLE IF NOT EXISTS news (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        url TEXT,
        timestamp TEXT
    )
''')
conn.commit()

def save_news(title, url):
    cur.execute("SELECT 1 FROM news WHERE url = ?", (url,))
    if not cur.fetchone():
        cur.execute(
            "INSERT INTO news (title, url, timestamp) VALUES (?, ?, ?)",
            (title, url, datetime.now().isoformat())
        )
        conn.commit()

def get_all_news():
    cur.execute("SELECT title, url, timestamp FROM news ORDER BY timestamp DESC")
    return cur.fetchall()
