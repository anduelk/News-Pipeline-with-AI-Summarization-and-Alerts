import sqlite3
from app.config import DB_FILE

def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS articles(
                   url TEXT PRIMARY KEY,
                   title TEXT
        )
    """)

    conn.commit()
    conn.close()


def save_articles(articles):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    new_count = 0

    for article in articles:
        url = article.get("url")
        title = article.get("title")

        try:
            cursor.execute(
                "INSERT INTO articles (url, title) VALUES (?, ?)",
                (url, title)
            )
            new_count += 1
        
        except sqlite3.IntegrityError:
            continue
        
    conn.commit()
    conn.close()

    return new_count




