from fastapi import FastAPI

# TestClient can help us with response testing
from fastapi.testclient import TestClient
from routers.auth import create_access_token

# from src.main import app
# import main as app
from main import app
import json
from datetime import timedelta, datetime
import random
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer



# python3 -m pytest testing/
# python3 -m pytest --cov=src --cov-report=html testing/


# Create an instance of the TestClient class
client = TestClient(app)

def test_post_create_user():
    # Make a POST request to the /user endpoint with the access token
    random_number = random.randint(1, 10000000000) 

    new_user = {
        "email": str(random_number) + "@test.com",
        "username": "test_user_" + str(random_number),
        "first_name": "test",
        "surname": "test",
        "password": "test",
        "is_active": True,
        "role": "admin",
    }
    response = client.post("/auth/", json=new_user)
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

