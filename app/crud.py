from sqlalchemy.orm import Session
from app import models, schemas

def create_task(db: Session, task: schemas.TaskCreate):
    db_task = models.Task(
        title=task.title,
        description=task.description,
        status=task.status,
        priority=task.priority
    )
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks(db: Session, status: str | None = None):
    query = db.query(models.Task)

    if status:
        query = query.filter(models.Task.status == status)
    
    return query.all()

def get_task_by_id(db: Session, task_id: int):
    return db.query(models.Task).filter(models.Task.id == task_id).first()

def update_task(db: Session, task_id: int, task_data: schemas.TaskUpdate):
    db_task = get_task_by_id(db, task_id)

    if not db_task:
        return None
    
    update_data = task_data.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(db_task, key, value)

    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, task_id: int):
    db_task = get_task_by_id(db, task_id)

    if not db_task:
        return None
    
    db.delete(db_task)
    db.commit()
    return db_task