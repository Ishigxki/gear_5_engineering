# Gear 5 Engineering API

**Gear 5 Engineering** is a lightweight task management REST API built with **FastAPI** and **PostgreSQL**. It provides a simple CRUD interface for tasks, perfect for learning backend development, API design, and database integration.

## 🚀 Key Features

- Create new tasks
- Retrieve all tasks
- Read a task by ID
- Update task titles
- Delete tasks
- Built with FastAPI, Pydantic, and PostgreSQL

## 📦 What’s Included

- `main.py` — FastAPI app with CRUD endpoints for tasks
- `database.py` — PostgreSQL connection setup using `psycopg2`
- `requirements.txt` — project dependencies

## 🧩 API Endpoints

- `GET /` — health check, confirms the API is running
- `GET /tasks` — returns all tasks
- `GET /tasks/{id}` — returns a task by ID
- `POST /tasks` — creates a new task
- `PUT /tasks/{id}` — updates an existing task title
- `DELETE /tasks/{id}` — deletes a task by ID

## 🛠️ Setup

1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Start your PostgreSQL server and create the database used by the app:
   - Database name: `gear5_tasks`
   - Adjust `database.py` if your connection settings differ

3. Run the app:
   ```bash
   uvicorn main:app --reload
   ```

4. Open the interactive API docs:
   ```text
   http://127.0.0.1:8000/docs
   ```

## ⚠️ Notes

- The current database connection settings are stored in `database.py` and assume a local PostgreSQL instance.
- For production use, move credentials into environment variables or a secure config file.

## 💡 Example request

Create a task with curl:
```bash
curl -X POST "http://127.0.0.1:8000/tasks" -H "Content-Type: application/json" -d '{"title": "Learn Gear 5 API"}'
```

## 👍 Why this project matters

This API is a great starting point for building more advanced backend services, adding authentication, or extending the task model with deadlines, status, and user assignments.
