from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float
from sqlalchemy.orm import relationship

from enum import Enum as PythonEnum
from sqlalchemy import Enum, Date


class Users(Base):
    __tablename__ = 'users'

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
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))


class GenericObject(Base):
    __tablename__ = 'generics'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)


# class PaymentTypeEnum(PythonEnum):
#     DEBITCARD = "DEBITCARD"
#     CREDITCARD = "CREDITCARD"

class PaymentType(Base):
    __tablename__ = 'payment_type'

    PaymentId = Column(Integer, primary_key=True, autoincrement=True)
    StreetAddress = Column(String)
    State = Column(String)
    ZipCode = Column(Integer)
    CardNumber = Column(Integer)
    Expiration = Column(String)
    CVV = Column(Integer)
    ProcessingTime = Column(Integer)
    Validated = Column(Boolean)
    RecipientId = Column(Integer)
    Type = Column(String)
    AccountBalance = Column(Integer, default=0)
    CardLimit = Column(Integer, default=0)
    CardBalance = Column(Integer, default=0)
    CardCompany = Column(String, default="")
    WeeklyTransactionCount = Column(Integer, default=0)
    TimeSinceLastTransaction = Column(Integer, default=0)

class Transactions(Base):
    __tablename__ = 'transactions'

    transaction_id = Column(Integer, primary_key=True, index=True,  autoincrement=True)
    iplocation_state = Column(String)
    iplocation_city = Column(String)
    transaction_amount = Column(Integer)
    # transaction_date = Column(Date)
    transaction_date = Column(String)
    processed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    payment_id = Column(Integer)   




