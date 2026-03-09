📚 Study Notes — FastAPI + PostgreSQL Backend Project
1️⃣ API Framework

We built our backend using FastAPI.

Concept:
An API framework lets applications communicate through HTTP requests.

Example request types:

Method	Purpose
GET	Retrieve data
POST	Create data
DELETE	Remove data
PUT/PATCH	Update data

Example endpoint:

@app.get("/tasks")
def get_tasks():
    return {"tasks": []}

This means:

GET /tasks

returns task data.

2️⃣ API Documentation

FastAPI automatically generates interactive documentation using Swagger UI.

You accessed it at:

http://127.0.0.1:8000/docs

This allows you to:

test endpoints

send requests

view responses

see API schemas

3️⃣ Database

We installed and used PostgreSQL.

Concept:
A database stores structured data in tables.

Example table:

id	title	created_at
1	study fastapi	timestamp
4️⃣ Database Management Tool

We interacted with PostgreSQL using pgAdmin.

pgAdmin allows you to:

create databases

run SQL

view tables

manage data

5️⃣ SQL (Structured Query Language)

SQL is used to interact with databases.

Examples we used:

Create Table
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    title TEXT NOT NULL
);
Insert Data
INSERT INTO tasks (title)
VALUES ('study fastapi');
Read Data
SELECT * FROM tasks;
Delete Data
DELETE FROM tasks WHERE title = 'study fastapi';
6️⃣ Python Database Driver

We installed:

psycopg2-binary

This allows Python to connect to PostgreSQL.

Example connection:

import psycopg2

connection = psycopg2.connect(
    host="localhost",
    database="gear5_tasks",
    user="postgres",
    password="password"
)
7️⃣ CRUD Operations

Your API now performs CRUD operations.

Operation	Meaning
Create	Add data
Read	Get data
Update	Modify data
Delete	Remove data

Your API currently supports:

Create tasks

Read tasks

Delete tasks

8️⃣ Data Models

We used Pydantic models to define request data.

Example:

from pydantic import BaseModel

class Task(BaseModel):
    title: str

This ensures incoming data is structured.

Example request body:

{
 "title": "Study FastAPI"
}
9️⃣ Running the API Server

We ran the server using:

uvicorn main:app --reload

This uses Uvicorn, an ASGI server for FastAPI.

--reload means the server restarts automatically when code changes.
