from pydantic import BaseModel

class ProjectCreate(BaseModel):
    name: str
    owner: str
    budget: float

class ProjectSchema(ProjectCreate):
    id: int

    class Config:
        orm_mode = True
