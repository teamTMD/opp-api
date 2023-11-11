from typing import Annotated

from fastapi import APIRouter, Depends, Path, HTTPException
from pydantic import BaseModel, Field
from starlette import status
from sqlalchemy.orm import Session

from routers.auth import get_current_user
from routers.helpers import check_user_authentication

from models.models import Transactions
from db.database import SessionLocal

router = APIRouter(prefix="/transactions", tags=["transactions"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

# when an API uses this, it will enforce authorization

# TC - DB dependency is enforeced when used in an API
user_dependency = Annotated[dict, (Depends(get_current_user))]


# class TodoRequest(BaseModel):
#     title: str = Field(min_length=3)
#     description: str = Field(min_length=3, max_length=100)
#     priority: int = Field(gt=0, lt=6)
#     complete: bool


class TransactionRequest(BaseModel):
    iplocation_city: str = Field(min_length=3)
    iplocation_state: str = Field(min_length=2)
    transaction_amount: int = Field(gt=0)
    transaction_date: str = Field(min_length=3)
    processed: bool


@router.get("/mytransactions")
async def read_all(user: user_dependency, db: db_dependency):
    check_user_authentication(user)
    return db.query(Transactions).filter(Transactions.user_id == user.get("id")).all()


@router.get("/userpending")
async def read_all(user: user_dependency, db: db_dependency):
    check_user_authentication(user)
    return (
        db.query(Transactions)
        .filter(Transactions.user_id == user.get("id"))
        .filter(Transactions.processed == False)
        .all()
    )


@router.post("/mytransactions", status_code=status.HTTP_201_CREATED)
async def create_transaction(
    user: user_dependency, db: db_dependency, transaction_request: TransactionRequest
):
    check_user_authentication(user)

    # transaction_model = Transactions(**transaction_request.model_dump(), user_id=user.get('id'))
    transaction_model = Transactions(
        **transaction_request.model_dump(), user_id=user.get("id")
    )

    db.add(transaction_model)
    db.commit()
