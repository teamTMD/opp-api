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


def test_get_read_all_authorized():

    # Create an access token for an authenticated user
    access_token = create_access_token(username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60))

    # Make a GET request to the /payment_type/read-all endpoint with the access token
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get("/payment_type/read-all", headers=headers)

    # Check if the response status code is 200 OK
    assert response.status_code == 200

def test_get_read_all_not_authorized():
    response = client.get("/payment_type/read-all")
    assert response.status_code == 401

def test_post_create_payment_type():
    # Create an access token for an authenticated user
    access_token = create_access_token(username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60))

    # Make a POST request to the /payment_type endpoint with the access token
    headers = {"Authorization": f"Bearer {access_token}"}
    new_payment_type = {
        "CardNumber": 123456789,
        "Expiration": "2021-12-12",
        "CVV": 123,
        "ProcessingTime": 123,
        "Validated": True,
        "RecipientId": 1,
        "Type": "test",
        "AccountBalance": 123
    }
    response = client.post("/payment_type/", headers=headers, json= new_payment_type)

    # Check if the response status code is 201 CREATED
    assert response.status_code == 201

def test_put_update_payment_type():
    # Create an access token for an authenticated user
    access_token = create_access_token(username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60))

    # Make a PUT request to the /payment_type endpoint with the access token
    headers = {"Authorization": f"Bearer {access_token}"}
    updated_payment_type = {
        "CardNumber": 88888888,
        "Expiration": "2021-12-12",
        "CVV": 123,
        "ProcessingTime": 123,
        "Validated": True,
        "RecipientId": 1,
        "Type": "test",
        "AccountBalance": 123
    }
    payment_type_id = 4
    response = client.put(f"/payment_type/{payment_type_id}", headers=headers, json= updated_payment_type)

    # Check if the response status code is 204 
    assert response.status_code == 204

def test_put_update_payment_type_failed():
    # Create an access token for an authenticated user
    access_token = create_access_token(username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60))

    # Make a PUT request to the /payment_type endpoint with the access token
    headers = {"Authorization": f"Bearer {access_token}"}
    updated_payment_type = {
        "CardNumber": 88888888,
        "Expiration": "2021-12-12",
        "CVV": 123,
        "ProcessingTime": 123,
        "Validated": True,
        "RecipientId": 1,
        "Type": "test",
        "AccountBalance": 123
    }
    payment_type_id = 500000
    response = client.put(f"/payment_type/{payment_type_id}", headers=headers, json=updated_payment_type)

    # Check if the response status code is 204 
    assert response.status_code == 404

# This works but is commented out because it deletes the payment type from the database
# def test_delete_payment_type_success():
#     # Create an access token for an authenticated user
#     access_token = create_access_token(username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60))

#     # Make a DELETE request to the /payment_type endpoint with the access token
#     headers = {"Authorization": f"Bearer {access_token}"}
#     payment_type_id = 3
#     response = client.delete(f"/payment_type/{payment_type_id}", headers=headers)

#     # Check if the response status code is 204 
#     assert response.status_code == 204

def test_delete_payment_type_failed():
    # Create an access token for an authenticated user
    access_token = create_access_token(username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60))

    # Make a DELETE request to the /payment_type endpoint with the access token
    headers = {"Authorization": f"Bearer {access_token}"}
    payment_type_id = 300000
    response = client.delete(f"/payment_type/{payment_type_id}", headers=headers)

    # Check if the response status code is 204 
    assert response.status_code == 404

def test_validate_card_valid():
    # Create an access token for an authenticated user
    access_token = create_access_token(username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60))

    headers = {"Authorization": f"Bearer {access_token}"}
    VALID_CARD = 4147202464191053

    response = client.post("/payment_type/validate-card", params={"card_number": VALID_CARD}, headers=headers)

    # Check if the response status code is 200
    assert response.status_code == 200

    # "success": "true", "msg": "card number is valid."
    assert response.json()["msg"] == "card number is valid."

def test_validate_card_invalid():
    # Create an access token for an authenticated user
    access_token = create_access_token(username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60))

    headers = {"Authorization": f"Bearer {access_token}"}
    VALID_CARD = 888

    response = client.post("/payment_type/validate-card", params={"card_number": VALID_CARD}, headers=headers)

    # Check if the response status code is 200
    assert response.status_code == 200

    expected_msg = "is invalid"

    # "success": "true", "msg": "card number is valid."
    assert expected_msg in response.text



def test_process_card_not_fradulent():
    # Create an access token for an authenticated user
    access_token = create_access_token(username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60))

    headers = {"Authorization": f"Bearer {access_token}"}
    VALID_CARD = 4147202464191053
    AMOUNT = 100.00

    response = client.post("/payment_type/process-card", params={"card_number": VALID_CARD, "amt": AMOUNT}, headers=headers)

    # Check if the response status code is 200

    # Define the expected message
    expected_msg = "Card number has sufficient funds and is not fradulent"

    # Check if the response "msg" matches the expected message
    assert expected_msg in response.text

def test_process_card_fradulent():
    # Create an access token for an authenticated user
    access_token = create_access_token(username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60))

    headers = {"Authorization": f"Bearer {access_token}"}
    VALID_CARD = 4147202464191053
    AMOUNT = 1000000000.00

    response = client.post("/payment_type/process-card", params={"card_number": VALID_CARD, "amt": AMOUNT}, headers=headers)

    # Check if the response status code is 200

    # Define the expected message
    expected_msg = "Insufficient funds and/or fraudulent card"

    # Check if the response "msg" matches the expected message
    assert expected_msg in response.text


