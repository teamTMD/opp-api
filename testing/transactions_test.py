from fastapi import FastAPI
from fastapi.testclient import TestClient
from routers.auth import create_access_token
from main import app
from datetime import timedelta, datetime

client = TestClient(app)



def test_post_transactions():
    access_token = create_access_token(username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60))
    headers = {"Authorization": f"Bearer {access_token}"}
    new_transaction = {
        "ipLocationCity": "Seattle", 
        "ipLocationState": "Washington", 
        "transactionAmount": 100, 
        "transactionDate": "09-10-90",
        "processed": True
    }
    response = client.post("transactions/mytransactions", headers=headers, json=new_transaction)
    assert response.status_code == 201

def test_get_my_transactions():
    
    # Create an access token for an authenticated user
    access_token = create_access_token(username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60))

    # Make a GET request to the /payment_type/read-all endpoint with the access token
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get("transactions/mytransactions/", headers=headers)

    # Check if the response status code is 200 OK
    assert response.status_code == 200
    
def test_get_pending_transactions():
    
    # Create an access token for an authenticated user
    access_token = create_access_token(username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60))

    # Make a GET request to the /payment_type/read-all endpoint with the access token
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get("transactions/userpending/", params={"userId": 1, "processed": False}, headers=headers)

    # Check if the response status code is 200 OK
    assert response.status_code == 200

