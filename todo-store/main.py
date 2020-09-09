from typing import List

from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session

import models
import schemas
from db import get_db
from environment import env

app = FastAPI(title="Todo Store")


@app.get("/todo/{id}", response_model=schemas.Todo)
def get_todo(id: int, db: Session = Depends(get_db)):
    return db.query(models.Todo).filter(models.Todo.id == id).first()


@app.get("/todo/", response_model=List[schemas.Todo])
def get_all_todos(db: Session = Depends(get_db)):
    return db.query(models.Todo).all()


@app.post("/todo/", response_model=schemas.Todo)
def create_todo(todo_create: schemas.TodoCreate, db: Session = Depends(get_db)):
    todo = models.Todo(**todo_create.dict())  # type: ignore
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo


@app.delete("/todo/{id}", response_model=schemas.Todo)
def get_todo(id: int, db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()
    if todo:
        db.delete(todo)
        db.commit()
    return todo


if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=env.todo_store_port, reload=True)


