from fastapi import FastAPI

from models import models
from db.database import engine
from routers import auth, todos, admin

# application
app = FastAPI()

# sets up database defined in engine
models.Base.metadata.create_all(bind=engine)

# Set API endpoints on router
app.include_router(auth.router)
app.include_router(todos.router)
app.include_router(admin.router)
app.include_router(cardType.router)