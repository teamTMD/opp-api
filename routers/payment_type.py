from typing import Annotated

from fastapi import APIRouter, Depends, Path, HTTPException
from pydantic import BaseModel, Field
from starlette import status
from sqlalchemy.orm import Session

from routers.auth import get_current_user
from routers.helpers import check_user_authentication

from models.models import PaymentType
from db.database import SessionLocal
from datetime import date
import requests


router = APIRouter(prefix="/payment_type", tags=["payment_type"])


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


class PaymentTypeRequest(BaseModel):
    # StreetAddress: str
    # State: str
    # ZipCode: int
    CardNumber: int
    Expiration: str
    CVV: int
    ProcessingTime: int
    Validated: bool
    RecipientId: int
    Type: str
    AccountBalance: int
    # CardLimit: int
    # CardBalance: int
    # CardCompany: str
    # WeeklyTransactionCount: int
    # TimeSinceLastTransaction: int


# Get all payment types
@router.get("/read-all")
async def read_all(user: user_dependency, db: db_dependency):
    check_user_authentication(user)
    return db.query(PaymentType).all()


# Update payment type by id
@router.put("/{payment_type_id}", status_code=status.HTTP_204_NO_CONTENT)
async def update_payment_type(
    user: user_dependency,
    db: db_dependency,
    payment_type_request: PaymentTypeRequest,
    payment_type_id: int = Path(gt=0),
):
    # why does json.loads throw 500 error
    check_user_authentication(user)

    payment_type_model = (
        db.query(PaymentType).filter(PaymentType.PaymentId == payment_type_id).first()
    )

    if payment_type_model is None:
        raise HTTPException(status_code=404, detail="Payment type not found")

    # make the updates
    payment_type_model.StreetAddress = payment_type_request.StreetAddress
    payment_type_model.State = payment_type_request.State
    payment_type_model.ZipCode = payment_type_request.ZipCode
    payment_type_model.CardNumber = payment_type_request.CardNumber
    payment_type_model.Expiration = payment_type_request.Expiration
    payment_type_model.CVV = payment_type_request.CVV
    payment_type_model.ProcessingTime = payment_type_request.ProcessingTime
    payment_type_model.Validated = payment_type_request.Validated
    payment_type_model.RecipientId = payment_type_request.RecipientId
    payment_type_model.Type = payment_type_request.Type
    payment_type_model.AccountBalance = payment_type_request.AccountBalance
    payment_type_model.CardLimit = payment_type_request.CardLimit
    payment_type_model.CardBalance = payment_type_request.CardBalance
    payment_type_model.CardCompany = payment_type_request.CardCompany
    payment_type_model.WeeklyTransactionCount = (
        payment_type_request.WeeklyTransactionCount
    )
    payment_type_model.TimeSinceLastTransaction = (
        payment_type_request.TimeSinceLastTransaction
    )

    db.add(payment_type_model)
    db.commit()


# Create post request for payment type
@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_payment_type(
    user: user_dependency, db: db_dependency, payment_type_request: PaymentTypeRequest
):
    check_user_authentication(user)

    payment_type_model = PaymentType(**payment_type_request.model_dump())

    db.add(payment_type_model)
    db.commit()


# Delete payment type by id
@router.delete("/{payment_type_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_payment_type(
    user: user_dependency, db: db_dependency, payment_type_id: int = Path(gt=0)
):
    # Update below to check if the user is an admin
    check_user_authentication(user)

    payment_type_model = (
        db.query(PaymentType).filter(PaymentType.PaymentId == payment_type_id).first()
    )
    if payment_type_model is None:
        raise HTTPException(status_code=404, detail="Payment type not found")
    db.query(PaymentType).filter(PaymentType.PaymentId == payment_type_id).delete()

    db.commit()


# Post reqeust to validate card number

VALIDATE_CARD_URL = (
    "https://c3jkkrjnzlvl5lxof74vldwug40pxsqo.lambda-url.us-west-2.on.aws"
)


@router.post("/validate-card", status_code=status.HTTP_200_OK)
async def validate_card_number(
    user: user_dependency, db: db_dependency, card_number: int
):
    # Test Valid Card Number: 4147202464191053
    # Test Invalid Card Number: 41472024641910

    check_user_authentication(user)
    # Convert card number to JSON format
    card_number = {"card_number": card_number}

    # Get response from lambda function
    response = requests.post(VALIDATE_CARD_URL, json=card_number)

    print(response.text)

    if response.status_code == 200:
        return response.json()
    else:
        return response.text
