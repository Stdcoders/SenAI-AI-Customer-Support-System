# SenAI - AI Powered Customer Support System

## Overview

SenAI is an AI-powered customer support platform that automates email triaging and customer support workflows using Large Language Models, Retrieval-Augmented Generation (RAG), and a Multi-Layer Intelligence Engine.

The system combines rule-based business logic with AI reasoning to classify emails, retrieve company knowledge, generate draft responses, analyze customer sentiment, and recommend escalations.

---

## Features

* Multi-Layer Intelligence Engine
* Autonomous ReAct Agent
* Retrieval Augmented Generation (RAG)
* Email Ingestion Pipeline
* Sentiment Trend Analysis
* Draft Reply Generation
* Dashboard & Analytics

---

## Tech Stack

### Backend

* FastAPI
* SQLAlchemy
* SQLite
* Gemini 2.5 Flash

### Frontend

* React
* Tailwind CSS
* Recharts

### AI

* ReAct Agent
* FAISS Vector Store
* RAG Pipeline

---

## Architecture

The project follows a layered architecture.

```
React Frontend

↓

FastAPI APIs

↓

Service Layer

↓

Repository Layer

↓

SQLite Database
```

### Architectural Decisions

* **Layered Architecture** for separation of concerns and maintainability.
* **Repository Pattern** to isolate database operations from business logic.
* **ReAct Agent** to provide transparent Thought → Action → Observation reasoning.
* **RAG Pipeline** to ground AI responses using company knowledge instead of relying only on LLM memory.
* **Multi-Layer Intelligence** combines deterministic heuristics with AI classification for better reliability.

---

## Project Structure

```
app/

agents/
api/
core/
db/
knowledge/
models/
repositories/
schemas/
services/

frontend/

docs/
storage/
```

---

## Database

The application is built around three primary entities:

```
Contact

↓

Thread

↓

Email
```

* One Contact owns multiple Threads.
* One Thread contains multiple Emails.

---

## API Endpoints

| Endpoint                       | Description          |
| ------------------------------ | -------------------- |
| POST /api/ingest               | Ingest new email     |
| GET /api/status/{job_id}       | Processing status    |
| GET /dashboard/stats           | Dashboard statistics |
| GET /threads/{contact_email}   | Conversation thread  |
| POST /respond/{email_id}       | Send response        |
| GET /rag/search                | Knowledge retrieval  |
| GET /contacts/{email}          | Contact profile      |
| GET /analytics/sentiment-trend | Sentiment analytics  |

---

## Setup

### Backend

```bash
pip install -r requirements.txt

uvicorn app.main:app --reload
```

Swagger

```
http://127.0.0.1:8000/docs
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## Future Improvements

* Authentication
* Background job processing
* Live email integration
* Cloud deployment
* Real-time notifications

---
