from fastapi import FastAPI, Depends, HTTPException , Query
from sqlalchemy.orm import Session

from app.database import SessionLocal, engine, Base
from app import schemas, crud

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="Task Manager API",
    description="A simple FastAPI project for managing tasks",
    version="1.0.0"
)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def read_root():
    return {"message": "Welcome to the Task Manager API"}

@app.post("/tasks", response_model=schemas.TaskResponse, status_code=201)
def create_task(task: schemas.TaskCreate, db: Session = Depends(get_db)):
    return crud.create_task(db, task)

@app.get("/tasks", response_model=list[schemas.TaskResponse])
def get_tasks(
    status: str | None = Query(default=None),
    db: Session = Depends(get_db)
):
    allowed_statuses = {"pending", "in_progress", "done"}

    if status is not None and status not in allowed_statuses:
        raise HTTPException(
            status_code=400,
            detail="Invalid status. Use pending, in_progress or done."
        )
    return crud.get_tasks(db, status)

@app.get("/tasks/{task_id}", response_model=schemas.TaskResponse)
def get_task(task_id: int, db: Session = Depends(get_db)):
    task = crud.get_task_by_id(db, task_id)

    if not task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return task

@app.put("/tasks/{task_id}", response_model=schemas.TaskResponse)
def update_task(task_id: int,task_data: schemas.TaskUpdate, db: Session = Depends(get_db)):
    updated_task = crud.update_task(db, task_id, task_data)

    if not updated_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return updated_task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int, db: Session = Depends(get_db)):
    deleted_task = crud.delete_task(db, task_id)

    if not deleted_task:
        raise HTTPException(status_code=404, detail="Task not found")
    
    return {"message": "Task deleted successfully"}
