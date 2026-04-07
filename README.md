# News Monitoring & AI Alert System

A production-style Python pipeline that fetches news, processes relevant articles, stores them in a database, enriches them with AI summaries, and sends notifications automatically.

---

# Overview

This project is designed as a **modular data pipeline system**:

```
FETCH → PROCESS → STORE → AI → NOTIFY → SCHEDULE
```

It demonstrates how real-world backend systems are structured and scaled.

---

# Features

### Core

* Fetch news from external API
* Filter articles by keywords
* Store articles in SQLite database
* Avoid duplicates using unique constraints

### AI Integration

* Summarize articles using AI (OpenAI-ready)
* Batch processing support
* Extendable to other AI providers

### Notifications

* Email alerts for new articles

### ⏱Automation

* Runs continuously using a scheduler

### Engineering Practices

* Modular architecture
* Separation of concerns
* Config-driven design
* Logging instead of print statements

---

# Project Structure

```id="6rqqcc"
news_monitor/
│
├── app/
│   ├── config.py
│   ├── logger.py
│   │
│   ├── clients/
│   │   └── api_client.py
│   │
│   ├── services/
│   │   ├── news_service.py
│   │   ├── processor.py
│   │   ├── storage_service.py
│   │   ├── notification_service.py
│   │   └── ai_service.py
│   │
│   └── scheduler.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# Architecture Explained

This project follows **layered architecture**:

### 1. Clients Layer

Handles communication with external systems (APIs)

### 2. Services Layer

Contains business logic:

* Fetching data
* Filtering
* AI processing
* Notifications

### 3. Storage Layer

Manages persistence using SQLite

### 4. Scheduler Layer

Controls execution timing

### 5. Entry Point

`main.py` orchestrates the entire pipeline

---

# Data Flow

1. Fetch latest news
2. Filter relevant articles
3. Store new articles (avoid duplicates)
4. Generate AI summaries
5. Send email notifications
6. Repeat on schedule

---

# Setup

## 1. Clone the repository

```
git clone <repo-url>
cd news_monitor
```

---

## 2. Install dependencies

```
pip install -r requirements.txt
```

---

## 3. Configure environment

Edit `app/config.py`:

```python id="cfg002"
API_KEY = "your_news_api_key"

EMAIL_SENDER = "your_email@gmail.com"
EMAIL_PASSWORD = "your_password"
EMAIL_RECEIVER = "receiver@gmail.com"
```

---

## Run the Application

```
python main.py
```


---

# Key Concepts

* API integration
* Data pipelines
* Modular system design
* Database usage
* AI service integration
* Automation & scheduling


