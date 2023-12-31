from datetime import timedelta, datetime

from fastapi import APIRouter, Depends, HTTPException, Path
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from pydantic import BaseModel
from starlette import status

from models.models import Users
from passlib.context import CryptContext
from db.database import SessionLocal
from typing import Annotated, Any
from sqlalchemy.orm import Session
from jose import jwt, JWTError

router = APIRouter(prefix="/auth", tags=["auth"])

import os
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

# These are used to create the signature for a JWT
# UPDATE AND MOVE TO .ENV

SECRET_KEY = "1696edacb812c9f1046065809ae02d8ce46e60ecc8e351b08284555c1bade7e4"
# SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"
# ALGORITHM = os.getenv('ALGORITHM')

bcrypt_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_bearer = OAuth2PasswordBearer(tokenUrl="auth/token")


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]


class CreateUserRequest(BaseModel):
    email: str
    username: str
    first_name: str
    surname: str
    password: str
    role: str


class Token(BaseModel):
    access_token: str
    token_type: str


@router.post("/", status_code=status.HTTP_201_CREATED)
async def create_user(db: db_dependency, create_user_request: CreateUserRequest):
    create_user_model = Users(
        email=create_user_request.email,
        username=create_user_request.username,
        first_name=create_user_request.first_name,
        surname=create_user_request.surname,
        role=create_user_request.role,
        hashed_password=bcrypt_context.hash(create_user_request.password),
        is_active=True,
    )

    db.add(create_user_model)
    db.commit()
    return {"Successfully created User!"}


@router.post("/token/", response_model=Token)
async def login_for_access_token(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: db_dependency
):
    print("Running post request for auth token")
    # Authenticate the user
    # TODO: check if form_data is validated by FastAPI
    user = authenticate_user(form_data.username, form_data.password, db)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user"
        )

    # Create token from the authenticated user
    token = create_access_token(
        user.username, user.id, user.role, timedelta(minutes=30)
    )

    return {"access_token": token, "token_type": "bearer"}


# TC - Getting called by login_for_access_token
def authenticate_user(username: str, password: str, db: db_dependency) -> Any:
    user = db.query(Users).filter(Users.username == username).first()
    if not user:
        return False
    if not bcrypt_context.verify(password, user.hashed_password):
        return False

    return user


# TC - Getting called by login_for_access_token
def create_access_token(
    username: str, user_id: int, role: str, expires_delta: timedelta
):
    claims = {"sub": username, "id": user_id, "role": role}
    expires = datetime.utcnow() + expires_delta
    claims.update({"exp": expires})
    token = jwt.encode(claims, SECRET_KEY, algorithm=ALGORITHM)
    return token


# TC - Getting current user called to verify user with JSON WEB TOKEN
async def get_current_user(token: Annotated[str, Depends(oauth2_bearer)]):
    # Need to make sure the current user has used an auth token else they should not have access
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # Extracting from the token all the info we need to see if the user is authorized
        username: str = payload.get("sub")
        user_id: int = payload.get("id")
        user_role: str = payload.get("role")
        if username is None or user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Could not validate user",
            )
        return {"username": username, "id": user_id, "user_role": user_role}
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Could not validate user"
        )


@router.delete("/delete_user", status_code=status.HTTP_201_CREATED)
async def delete_user(db: db_dependency, username: str):
    user_model = db.query(Users).filter(Users.username == username).first()
    if user_model is None:
        raise HTTPException(status_code=404, detail="User not found")
    db.query(Users).filter(Users.username == username).delete()
    db.commit()
    return {"Successfully deleted user."}