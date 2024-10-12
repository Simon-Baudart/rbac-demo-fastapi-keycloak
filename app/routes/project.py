from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas
from app.database import get_db

router = APIRouter()

# Créer un projet
@router.post("/projects/", response_model=schemas.ProjectSchema)
def create_new_project(project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    return crud.create_project(db, project)

# Lire tous les projets
@router.get("/projects/", response_model=List[schemas.ProjectSchema])
def list_projects(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return crud.get_projects(db, skip=skip, limit=limit)

# Lire un projet par ID
@router.get("/projects/{project_id}", response_model=schemas.ProjectSchema)
def read_project(project_id: int, db: Session = Depends(get_db)):
    db_project = crud.get_project(db, project_id)
    if db_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return db_project

# Mettre à jour un projet
@router.put("/projects/{project_id}", response_model=schemas.ProjectSchema)
def modify_project(project_id: int, project: schemas.ProjectCreate, db: Session = Depends(get_db)):
    updated_project = crud.update_project(db, project_id, project)
    if updated_project is None:
        raise HTTPException(status_code=404, detail="Project not found")
    return updated_project

# Supprimer un projet
@router.delete("/projects/{project_id}")
def remove_project(project_id: int, db: Session = Depends(get_db)):
    success = crud.delete_project(db, project_id)
    if not success:
        raise HTTPException(status_code=404, detail="Project not found")
    return {"message": "Project deleted successfully"}
