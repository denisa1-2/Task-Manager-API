# Task-Manager-API

A simple REST API built with FastAPI for managing tasks.

## Features

- Create a task
- Gret all tasks
- Filter tasks by status
- Get a task by ID
- Update a task
- Delete a task

## Tech Stack

- Python
- FastAPI
- SQLAlchemy
- SQLite
- Pydantic

## Project Structure

```bash
task-manager-api/
|
|- app/
|   |- __init__.py
|   |- crud.py
|   |- database.py
|   |- main.py
|   |- models.py
|   |- schemas.py
|
|- requirements.py
```

## Installation

1. Clone the repository
2. Create a virtual environment
3. Install dependencies
```bash
pip install - r requirements.txt
```

## Run the Project

```bash
uvicorn app.main:app --reload
```

## API Documentation

After running the server, open:
```bash
http://127.0.0.1:8000/docs
```

## Exemple Task

{
  "title": "Learn FastAPI",
  "description": "Build my first backend project",
  "status": "pending",
  "priority": 2
}
