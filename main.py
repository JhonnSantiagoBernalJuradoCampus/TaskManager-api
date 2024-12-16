from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas, crud
from database import engine, SessionLocal
import json
import base64
from io import BytesIO
from fastapi.middleware.cors import CORSMiddleware


models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def initialize_tasks():
    db = SessionLocal()
    if db.query(models.Task).count() == 0:
        task1 = models.Task(title="Crear repo", description="Se requiere crear un repositorio en github para gestionar las versiones del proyecto de task manager", completed=False)
        task2 = models.Task(title="Presentacion", description="Se debe realizar la presentación del proyecto y validar que todo este correcto", completed=False)
        db.add_all([task1, task2])
        db.commit()
        print("Tareas iniciales agregadas")
    db.close()

initialize_tasks()

@app.get("/tasks/", response_model=list[schemas.TaskResponse])
def list_tasks(db: Session = Depends(get_db)):
    return crud.get_tasks(db=db)

@app.post("/tasks/", response_model=schemas.TaskResponse)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db=db, task=task)

@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int, task_update: schemas.TaskUpdate, db: Session = Depends(get_db)):
    updated_task = crud.mark_task_completed(db=db, task_id=task_id, completed=task_update.completed)
    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    return updated_task

@app.delete("/tasks/completed/")
def delete_completed(db: Session = Depends(get_db)):
    crud.delete_completed_tasks(db=db)
    return {"message": "Completed tasks have been deleted"}

@app.get("/tasks/export/")
def export_tasks(db: Session = Depends(get_db)):
    tasks = crud.get_tasks(db=db)

    tasks_data = [
        {"id": task.id, "title": task.title, "description": task.description, "completed": task.completed}
        for task in tasks
    ]

    buffer = BytesIO()
    json.dump(tasks_data, buffer, ensure_ascii=False, indent=4)
    buffer.seek(0) 
    
    encoded_file = base64.b64encode(buffer.read()).decode('utf-8')
    
    return {
        "filename": "tasks_export.json",
        "filedata": encoded_file,
        "message": "Tasks exported successfully as Base64"
    }
