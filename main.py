from app.clients.api_client import APIClient
from app.services.news_service import fetch_news
from app.services.processor import filter_articles
from app.services.storage_service import init_db, save_articles
from app.service.notification import send_email
from app.scheduler import run_forever
from app.config import BASE_URL, CHECK_INTERVAL

def pipeline():
    client = APIClient(BASE_URL)
    data = fetch_news(client)
    articles = filter_articles(data)
    new_count = save_articles(articles)
    if new_count > 0:
        send_email(articles)
    
    print(f"new article: {new_count}")

if __name__ == "__main__":
    init_db()
    run_forever(pipeline, CHECK_INTERVAL)

