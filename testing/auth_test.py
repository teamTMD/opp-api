from fastapi import FastAPI, Depends

# TestClient can help us with response testing
from fastapi.testclient import TestClient
from routers.auth import create_access_token, authenticate_user, get_db

# from src.main import app
# import main as app
from main import app
import json
from datetime import timedelta, datetime
import random
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from db.database import SessionLocal
from typing import Annotated, Any
from sqlalchemy.orm import Session




# python3 -m pytest testing/
# python3 -m pytest --cov=src --cov-report=html testing/


# Create an instance of the TestClient class
client = TestClient(app)

def test_post_create_user():
    # Make a POST request to the /user endpoint with the access token
    # random_number = random.randint(1, 10000000000) 

    new_user = {
        "email": "test@test.com",
        "username": "test_user",
        "first_name": "test",
        "surname": "test",
        "password": "test",
        "is_active": True,
        "role": "admin",
    }
    response = client.post("/auth/", json=new_user)
    assert response.status_code == 201
    response = client.delete("/auth/delete_user", params={"username": "test_user"})
    assert response.status_code == 201

def test_post_token():

    #form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
    # Create form data 
    form_data = {
        "username": "developer",
        "password": "developer",
    }
    response = client.post("/auth/token/", data=form_data)
    print(response.json())
    assert response.status_code == 200


# def test_authenticate_user():
#     # authenticate_user(username: str, password: str, db: db_dependency)
#     db_dependency = Annotated[Session, Depends(get_db)]
#     user = authenticate_user(username="test", password="test", db=db_dependency)

