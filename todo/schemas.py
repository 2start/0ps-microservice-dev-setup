from pydantic import BaseModel


class TodoCreate(BaseModel):
    title: str
    description: str


class Todo(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True
