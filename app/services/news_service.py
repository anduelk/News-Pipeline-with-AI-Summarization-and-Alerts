from typing import Dict, Any
from app.config import API_KEY, COUNTRY
from app.clients.api_client import APIClient

def fetch_news(client: APIClient) -> Dict[str, Any]:
    params = {
        "api_key": API_KEY,
        "country": COUNTRY
        }
    
    return client.get("/top-headlines", params=params)

