from datetime import timedelta

from jose import jwt, JWTError
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from db.database import SessionLocal
from main import app
from fastapi.testclient import TestClient

from models.models import Users
from routers.auth import bcrypt_context, get_db, SECRET_KEY, ALGORITHM

client = TestClient(app)

#--------------------TEST CREATE USER--------------------#
def test_create_user():
    # Test data for creating an instance of a user
    test_user_data = {
        "email": "user_test",
        "username": "user_test",
        "first_name": "user_test",
        "surname": "user_test",
        "password": "user_test",
        "role": "user",
    }

    # Assuming you have a database URL
    DATABASE_URL = "sqlite:///./payment_app.db"

    # Create the database engine
    engine = create_engine(DATABASE_URL)

    # Create a factory for creating new sessions
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    #assertions
    with engine.connect() as connection:
        SessionLocal.configure(bind=connection)
        session = SessionLocal()
        created_user = session.query(Users).filter_by(email=test_user_data["email"]).first()

        assert created_user is not None
        assert created_user.email == test_user_data["email"]
        assert created_user.username == test_user_data["username"]
        assert created_user.first_name == test_user_data["first_name"]
        assert created_user.surname == test_user_data["surname"]
        assert created_user.role == test_user_data["role"]
        # You might want to hash the password and compare it if it's hashed in the database
        assert bcrypt_context.verify(test_user_data["password"], created_user.hashed_password)

# Define your test database
TEST_DATABASE_URL = "sqlite:///:memory:"
engine = create_engine(TEST_DATABASE_URL)

# Function to override default dependency for testing
def override_get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

app.dependency_overrides[get_db] = override_get_db

client = TestClient(app)



#--------------------TEST LOGIN FOR ACCESS TOKEN--------------------#
# def test_login_for_access_token():
#     # Test data for login
#     test_user_data = {
#         "username": "test_user",
#         "password": "test_user",
#     }
#
#     # Create a test user in the database
#     with SessionLocal() as session:
#         hashed_password = bcrypt_context.hash(test_user_data["password"])
#         test_user = Users(
#             username=test_user_data["username"],
#             hashed_password=hashed_password,
#             role="user",
#         )
#         session.add(test_user)
#         session.commit()
#
#     # Make a request to the login_for_access_token endpoint using the TestClient
#     response = client.post("/auth/token", data=test_user_data)
#
#     # Assert that the response has a successful status code
#     assert response.status_code == 200
#
#     # Assert that the response has the expected structure
#     response_json = response.json()
#     assert "access_token" in response_json
#     assert "token_type" in response_json
#
#     # Decode the access token and assert its properties
#     decoded_token = decode_access_token(response_json["access_token"])
#     assert decoded_token["sub"] == test_user_data["username"]
#     # ... add more assertions based on your token structure
#
# def decode_access_token(token):
#     # Decode the access token for assertions
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload
#     except JWTError:
#         return None


#TODO

#--------------------TEST AUTHENTICATE USER--------------------#
def test_authenticate_user():
    # Test data for creating an instance of a user
    test_user_data = {
        "email": "user_test",
        "username": "user_test",
        "first_name": "user_test",
        "surname": "user_test",
        "password": "user_test",
        "role": "user",
    }

    # Assuming you have a database URL
    DATABASE_URL = "sqlite:///./payment_app.db"

    # Create the database engine
    engine = create_engine(DATABASE_URL)

    # Create a factory for creating new sessions
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # assertions
    with engine.connect() as connection:
        SessionLocal.configure(bind=connection)

        response = client.post("/auth/token", data=test_user_data)

        # Assert that the response has a successful status code
        assert response.status_code == 200

        # Assert that the response has the expected structure
        response_json = response.json()
        assert "access_token" in response_json
        assert "token_type" in response_json

#--------------------TEST CREATE ACCESS TOKEN--------------------#
# def test_create_access_token():
#     # Test data for creating an access token
#     test_user_data = {
#         "username": "test_user",
#         "user_id": 1,
#         "role": "user",
#     }

    # Set an expiration time for the token
    # expires_delta = timedelta(minutes=30)

    # Make a request to the create_access_token endpoint using the TestClient
    # response = client.post("/auth/token", data=test_user_data, )

    # Assert that the response has a successful status code
    # assert response.status_code == 200

    # # Assert that the response has the expected structure
    # response_json = response.json()
    # assert "access_token" in response_json
    # assert "token_type" in response_json
    #
    # # Decode the access token and assert its properties
    # decoded_token = decode_access_token(response_json["access_token"])
    # assert decoded_token["sub"] == test_user_data["username"]
    # assert decoded_token["id"] == test_user_data["user_id"]
    # assert decoded_token["role"] == test_user_data["role"]

# def decode_access_token(token):
#     # Decode the access token for assertions
#     try:
#         payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
#         return payload
#     except JWTError:
#         return None

def test_get_current_user():
    pass