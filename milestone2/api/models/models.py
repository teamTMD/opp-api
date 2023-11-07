from db.database import Base
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey, Float, DateTime


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
    
class Transactions(Base):
    __tablename__ = 'transactions'
    
    transaction_id = Column(Integer, primary_key=True, index=True)
    iplocation_state = Column(String)
    iplocation_city = Column(String)
    transaction_amount = Column(Integer)
    transaction_date = Column(DateTime)
    processed = Column(Boolean, default=False)
    user_id = Column(Integer, ForeignKey("users.id"))
    payment_id = Column(Integer)    
    
    
class GenericObject(Base):
    __tablename__ = 'generics'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    price = Column(Float)







