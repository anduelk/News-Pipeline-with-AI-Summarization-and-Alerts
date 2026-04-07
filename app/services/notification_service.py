import smtplib
from app.config import EMAIL_SENDER, EMAIL_PASSWORD, EMAIL_RECEIVER

def send_email(articles):
    if not articles:
        return None
    
    content = "\n".join(a.get("title", "") for a in articles)

    message = f"Subject: new content\n\n{content}"

    with smtplib.SMTP("smtp.gmail.com", 837) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, message)


