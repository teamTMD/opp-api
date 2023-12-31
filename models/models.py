from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

from enum import Enum as PythonEnum
from sqlalchemy import Enum, Date
from datetime import date



class Users(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True)
    username = Column(String, unique=True)
    first_name = Column(String)
    surname = Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)
    role = Column(String)
    phone_number = Column(String)


class Todos(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))


class GenericObject(Base):
    __tablename__ = "generics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)


# class PaymentTypeEnum(PythonEnum):
#     DEBITCARD = "DEBITCARD"
#     CREDITCARD = "CREDITCARD"


class PaymentType(Base):
    __tablename__ = "payment_type"

    PaymentId = Column(Integer, primary_key=True, autoincrement=True)
    CardNumber = Column(Integer)
    Expiration = Column(String)
    CVV = Column(Integer)
    ProcessingTime = Column(Integer)
    Validated = Column(Boolean)
    RecipientId = Column(Integer)
    # Convert to lower case
    Type = Column(String)
    AccountBalance = Column(Integer, default=0)
    # CardLimit = Column(Integer, default=0)
    # CardBalance = Column(Integer, default=0)
    # WeeklyTransactionCount = Column(Integer, default=0)
    # TimeSinceLastTransaction = Column(Integer, default=0)


class Transactions(Base):
    __tablename__ = "transactions"

    transactionId = Column(Integer, primary_key=True, index=True, autoincrement=True)
    ipLocationCity = Column(String)
    ipLocationState = Column(String)
    transactionAmount = Column(Integer)
    transactionDate = Column(Date)
    processed = Column(Boolean, default=False)
    userId = Column(Integer, ForeignKey("users.id"))
