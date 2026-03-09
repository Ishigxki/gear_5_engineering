## main.py
from fastapi import FastAPI
from database import connection,cursor

# Create a FastAPI app instance
app = FastAPI()

@app.get("/")
def home():
    return {"message":"Gear 5 Api running"}

# Define a GET endpoint at the root URL "/"
@app.get("/tasks")
def get_tasks():
    cursor.execute("SELECT * FROM tasks;")
    rows = cursor.fetchall()
    return {"tasks": rows}
@app.post("/tasks")
def create_task(task:str):
    cursor.execute("INSERT INTO tasks (title) VALUES (%s) RETURNING id;",(task,))
    connection.commit()
    return {"message": "Task created"}

@app.delete("/tasks")
def remove_task(task:str):
    cursor.execute("DELETE FROM tasks WHERE title = %s;", (task,))
    connection.commit()
    return {"message": "Task deleted"}