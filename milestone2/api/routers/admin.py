from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from starlette import status
from sqlalchemy.orm import Session
from routers.auth import get_current_user

from models.models import Users, Todos, Transactions
from db.database import SessionLocal

router = APIRouter(prefix='/admin', tags=['admin'])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

# when an API uses this, it will enforce authorization
user_dependency = Annotated[dict, (Depends(get_current_user))]


@router.get("/todo",status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    check_admin_user_auth(user)
    return db.query(Todos).all()

@router.get("/todo",status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    check_admin_user_auth(user)
    return db.query(Todos).all()

@router.get("/transactions",status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    check_admin_user_auth(user)
    return db.query(Transactions).all()

@router.get("/pending",status_code=status.HTTP_200_OK)
async def read_all(user: user_dependency, db: db_dependency):
    check_admin_user_auth(user)
    # db.query(Transactions).
    return db.query(Transactions).filter(Transactions.processed == False).all()


def check_admin_user_auth(user):
    # Fixed Typo
    if user is None or user.get('user_role').lower() != 'admin':
        raise HTTPException(status_code=401, detail='Authentication Failed')