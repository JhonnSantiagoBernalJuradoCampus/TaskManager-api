from pydantic import BaseModel

class TaskBase(BaseModel):
    title: str
    description: str | None = None

class TaskCreate(TaskBase):
    pass

class TaskUpdate(BaseModel):
    completed: bool

class TaskResponse(TaskBase):
    id: int
    completed: bool

    class Config:
        orm_mode = True
