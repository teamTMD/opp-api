from typing import Annotated

from fastapi import APIRouter, Depends, Path, HTTPException
from pydantic import BaseModel, Field
from starlette import status
from sqlalchemy.orm import Session

from routers.auth import get_current_user
from routers.helpers import check_user_authentication

from models.models import Users
from db.database import SessionLocal

router = APIRouter(prefix="/customers", tags=["customers"])


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

# when an API uses this, it will enforce authorization
user_dependency = Annotated[dict, (Depends(get_current_user))]


# Return all business owners
@router.get("/business-owners", status_code=status.HTTP_200_OK)
async def read_all_business_owners(user: user_dependency, db: db_dependency):
    check_user_authentication(user)
    return db.query(Users).filter(Users.role == "business_owner").all()


# Return all developers
@router.get("/developers", status_code=status.HTTP_200_OK)
async def read_all_developers(user: user_dependency, db: db_dependency):
    check_user_authentication(user)
    return db.query(Users).filter(Users.role == "developer").all()


# Delete customer by id
@router.delete("/customer/{customer_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer(
    user: user_dependency, db: db_dependency, customer_id: int = Path(gt=0)
):
    # Update below to check if the user is an admin
    check_user_authentication(user)

    customer_model = db.query(Users).filter(Users.id == customer_id).first()
    if customer_model is None:
        raise HTTPException(status_code=404, detail="Customer not found")
    db.query(Users).filter(Users.id == customer_id).delete()

    db.commit()


# @router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
#     check_user_authentication(user)

#     todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get('id')).first()
#     if todo_model is None:
#         raise HTTPException(status_code=404, detail='Todo not found')
#     db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get('id')).delete()

#     db.commit()


# # Update user password by id
# @router.put("/update-user-password/{user_id}", status_code=status.HTTP_200_OK)
# async def update_user_password(user: user_dependency, db: db_dependency, user_id: int = Path(gt=0)):

#     # Update below to check that it is the same user
#     check_user_authentication(user)

#     user_model = (
#         db.query(Users).filter(Users.id == user_id).filter(Users.id == user.get('id')).first()
#     )
#     if user_model is not None:
#         return user_model
#     raise HTTPException(status_code=404, detail='User not found')
