## main.py
from fastapi import FastAPI
from pydantic import BaseModel
from database import connection,cursor


app = FastAPI()
# Create a FastAPI app instance
class Task(BaseModel):
    title: str

@app.get("/")
def home():
    return {"message": "Gear 5 API running"}

# Define a GET endpoint at the root URL "/"
@app.get("/tasks")
def get_tasks():
    cursor.execute("SELECT * FROM tasks;")
    rows = cursor.fetchall()
    tasks = []
    for row in rows:
        tasks.append({"id": row[0],"title":row[1]})

    return {"tasks": tasks}
@app.get("/tasks/{id}")
def get_tasks_by_id(id:int):
    cursor.execute("SELECT * FROM tasks WHERE id=%s;",(id,))
    rows= cursor.fetchone()
    if rows is None:
        return {"error": "Task not found"}

    return {"tasks": {"id":rows[0],"title":rows[1]}}

@app.put("/tasks/{id}")
def update_task(id: int, task: Task):
    cursor.execute(
        "UPDATE tasks SET title = %s WHERE id = %s;",
        (task.title, id)
    )
    connection.commit()
    return {"message": "Task updated"}
    

@app.post("/tasks")
def create_task(task: Task):
    cursor.execute(
        "INSERT INTO tasks (title) VALUES (%s);",
        (task.title,)
    )
    connection.commit()
    return {"message": "Task created"}

@app.delete("/tasks/{id}")
def delete_task(id: int):
    cursor.execute(
        "DELETE FROM tasks WHERE id = %s;",
        (id,)
    )
    connection.commit()

    if cursor.rowcount ==0:
        return {"error":"Task not found"}
    return {"message": "Task deleted"}