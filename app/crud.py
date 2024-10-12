from sqlalchemy.orm import Session
from app import models, schemas

# Créer un projet
def create_project(db: Session, project: schemas.ProjectCreate):
    db_project = models.Project(name=project.name, owner=project.owner, budget=project.budget)
    db.add(db_project)
    db.commit()
    db.refresh(db_project)
    return db_project

# Lire tous les projets
def get_projects(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Project).offset(skip).limit(limit).all()

# Lire un projet par ID
def get_project(db: Session, project_id: int):
    return db.query(models.Project).filter(models.Project.id == project_id).first()

# Mettre à jour un projet
def update_project(db: Session, project_id: int, project_data: schemas.ProjectCreate):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if db_project:
        db_project.name = project_data.name
        db_project.owner = project_data.owner
        db_project.budget = project_data.budget
        db.commit()
        db.refresh(db_project)
        return db_project
    return None

# Supprimer un projet
def delete_project(db: Session, project_id: int):
    db_project = db.query(models.Project).filter(models.Project.id == project_id).first()
    if db_project:
        db.delete(db_project)
        db.commit()
        return True
    return False
