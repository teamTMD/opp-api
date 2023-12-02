from fastapi import FastAPI

# TestClient can help us with response testing
from fastapi.testclient import TestClient
from routers.auth import create_access_token

# from src.main import app
# import main as app
from main import app
import json
from datetime import timedelta, datetime

# python3 -m pytest testing/
# python3 -m pytest --cov=src --cov-report=html testing/


# Create an instance of the TestClient class
client = TestClient(app)

# Import the db object
from db.database import SessionLocal

db = SessionLocal()
# Import Users model
from models.models import Users


def test_get_read_all_business_owners():
    # Create an access token for an authenticated user
    access_token = create_access_token(
        username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60)
    )

    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get("/customers/business-owners", headers=headers)
    expected_result = db.query(Users).filter(Users.role == "business_owner").all()

    for user in expected_result:
        assert user.role == "business_owner"
    assert response.status_code == 200


def test_get_read_all_developers():
    # Create an access token for an authenticated user
    access_token = create_access_token(
        username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60)
    )

    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get("/customers/developers", headers=headers)
    expected_result = db.query(Users).filter(Users.role == "developer").all()
    for user in expected_result:
        assert user.role == "developer"
    assert response.status_code == 200


# Test successfull but commented out to avoid deleting data from the database
# def test_delete_customer_by_id():
#         # Create an access token for an authenticated user
#         access_token = create_access_token(username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60))
#         headers = {"Authorization": f"Bearer {access_token}"}
#         response = client.delete("/customers/customer/1", headers=headers)
#         assert response.status_code == 204
