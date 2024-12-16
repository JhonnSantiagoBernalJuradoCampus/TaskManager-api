from sqlalchemy.orm import Session
import models, schemas

def get_tasks(db: Session):
    return db.query(models.Task).all()

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def mark_task_completed(db: Session, task_id: int, completed: bool):
    db_task = db.query(models.Task).filter(models.Task.id == task_id).first()
    if db_task:
        db_task.completed = completed
        db.commit()
        db.refresh(db_task)
    return db_task

def delete_completed_tasks(db: Session):
    db.query(models.Task).filter(models.Task.completed == True).delete()
    db.commit()
