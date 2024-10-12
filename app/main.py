from fastapi import FastAPI
from app.routes import project
from app.database import engine
from app import models

# Créer les tables de la base de données si elles n'existent pas
models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Inclure les routes de projets
app.include_router(project.router)

# Point de démarrage de l'application
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
