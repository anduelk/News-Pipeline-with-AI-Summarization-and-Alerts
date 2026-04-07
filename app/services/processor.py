from app.config import KEYWORDS

def filtered_articles(data):
    if not data or "articles" not in data:
        return []
    
    results = []

    for article in data["articles"]:
        title = article.get("title", "")
        description = article.get("description", "")

        text = f"{title} {description}".lower()

        for keywords in KEYWORDS:
            if keywords.lower() in text:
                results.append(article)
        
        return results
    
    
