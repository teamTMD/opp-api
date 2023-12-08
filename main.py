from fastapi import FastAPI

from models import models
from db.database import engine
from routers import auth, admin, customers, payment_type, transactions

from fastapi.middleware.cors import CORSMiddleware
from fastapi.exceptions import RequestValidationError
from fastapi.responses import PlainTextResponse 
# application
app = FastAPI()

# sets up database defined in engine
models.Base.metadata.create_all(bind=engine)

# Set API endpoints on router
app.include_router(auth.router)
app.include_router(customers.router)
app.include_router(transactions.router)
app.include_router(admin.router)
app.include_router(payment_type.router)

# Potentially Add CORS here

app.add_middleware(
    CORSMiddleware, 
    allow_origins=["*"], 
    allow_credentials=True, 
    allow_methods=["*"], 
    allow_headers=["*"],
)

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request, exc): 
    return PlainTextResponse(str(exc), status_code=422)