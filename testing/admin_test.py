from fastapi import FastAPI
from fastapi.testclient import TestClient
from routers.auth import create_access_token
from main import app
from datetime import timedelta, datetime

client = TestClient(app)


def test_check_admin_user_auth():
    # Create an access token for an authenticated user
    access_token = create_access_token(
        username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60)
    )

    # Make a GET request to the /payment_type/read-all endpoint with the access token
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get("admin/users/", headers=headers)

    assert response.status_code == 200


def test_check_admin_bad_user_auth():
    # Create an access token for an authenticated user
    access_token = create_access_token(
        username="test", user_id=1, role="user", expires_delta=timedelta(minutes=60)
    )

    # Make a GET request to the /payment_type/read-all endpoint with the access token
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get("admin/users/", headers=headers)

    assert response.status_code == 401
    assert response.json() == {"detail": "Authentication Failed"}


def test_check_admin_no_user_auth():
    # Create an access token for an authenticated user
    access_token = create_access_token(
        username="test", user_id=1, role="", expires_delta=timedelta(minutes=60)
    )

    # Make a GET request to the /payment_type/read-all endpoint with the access token
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get("admin/users/", headers=headers)

    assert response.status_code == 401
    assert response.json() == {"detail": "Authentication Failed"}


def test_get_users():
    # Create an access token for an authenticated user
    access_token = create_access_token(
        username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60)
    )

    # Make a GET request to the /payment_type/read-all endpoint with the access token
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get("admin/users/", headers=headers)

    # Check if the response status code is 200 OK
    assert response.status_code == 200


def test_get_transactions():
    # Create an access token for an authenticated user
    access_token = create_access_token(
        username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60)
    )

    # Make a GET request to the /payment_type/read-all endpoint with the access token
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get(
        "admin/transactions/", params={"role": "admin"}, headers=headers
    )

    # Check if the response status code is 200 OK
    assert response.status_code == 200


def test_get_pending():
    # Create an access token for an authenticated user
    access_token = create_access_token(
        username="test", user_id=1, role="admin", expires_delta=timedelta(minutes=60)
    )

    # Make a GET request to the /payment_type/read-all endpoint with the access token
    headers = {"Authorization": f"Bearer {access_token}"}
    response = client.get(
        "admin/pending/", params={"role": "admin", "processed": False}, headers=headers
    )

    # Check if the response status code is 200 OK
    assert response.status_code == 200
