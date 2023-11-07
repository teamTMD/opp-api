from typing import Annotated

from fastapi import APIRouter, Depends, Path, HTTPException
from pydantic import BaseModel, Field
from starlette import status
from sqlalchemy.orm import Session

from routers.auth import get_current_user
from routers.helpers import check_user_authentication

from models.models import Todos
from db.database import SessionLocal
# needed to associate a card to.
from models.models import Users

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[Session, Depends(get_db)]

# when an API uses this, it will enforce authorization

# TC - DB dependency is enforced when used in an API
user_dependency = Annotated[dict, (Depends(get_current_user))]





# TODO -- ReST API for Cards, debit/credit
# use User db for card id storage or a Card db for storage of card numbers?

# TODO -- get debit...how to define a card type based on user?  should the db be for card numbers or car type then sub category of type?
@router.get("/debit_card", status_code=status.HTTP_200_OK)
async def read_all_debit_cards(user: user_dependency, db: db_dependency):
    check_user_authentication(user)
    # how does the below get changed for the card functionality?
    return db.query(Users).filter(Users.role == 'user').all()

# TODO -- get credit
# this should model the above, but for a credit card.

# TODO -- delete debit
@router.delete("/customer/{customer_card}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_customer_card(user: user_dependency, db: db_dependency, customer_card: int = Path(gt=0)):
    # Update below to check if the user is an admin
    check_user_authentication(user)

    customer_model = db.query(Users).filter(Users.id == customer_id).first()
    if customer_model is None:
        raise HTTPException(status_code=404, detail='Customer not found')
    db.query(Users).filter(Users.id == customer_id).delete()

    db.commit()

# TODO -- delete credit
# do not believe to to be needed as a card could be selected from teh db then processed first?











# class TodoRequest(BaseModel):
#     title: str = Field(min_length=3)
#     description: str = Field(min_length=3, max_length=100)
#     priority: int = Field(gt=0, lt=6)
#     complete: bool
#
#
# @router.get("/read-all")
# async def read_all(user: user_dependency, db: db_dependency):
#     check_user_authentication(user)
#     return db.query(Todos).filter(git Todos.owner_id == user.get('id')).all()
#
#
# @router.get("/todo/{todo_id}", status_code=status.HTTP_200_OK)
# async def read_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
#     check_user_authentication(user)
#
#     todo_model = (
#         db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get('id')).first()
#     )
#
#     if todo_model is not None:
#         return todo_model
#     raise HTTPException(status_code=404, detail='Todo not found')
#
#
# @router.post("/todo", status_code=status.HTTP_201_CREATED)
# async def create_todo(user: user_dependency, db: db_dependency, todo_request: TodoRequest):
#     check_user_authentication(user)
#
#     todo_model = Todos(**todo_request.model_dump(), owner_id=user.get('id'))
#
#     db.add(todo_model)
#     db.commit()
#
#
# @router.put("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def update_todo(user: user_dependency, db: db_dependency,
#                       todo_request: TodoRequest,
#                       todo_id: int = Path(gt=0)):
#     # why does json.loads throw 500 error
#     check_user_authentication(user)
#
#     todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get('id')).first()
#
#     if todo_model is None:
#         raise HTTPException(status_code=404, detail="Todo not found")
#
#     # make the updates
#     todo_model.title = todo_request.title
#     todo_model.description = todo_request.description
#     todo_model.priority = todo_request.priority
#     todo_model.complete = todo_request.complete
#
#     db.add(todo_model)
#     db.commit()
#
#
# @router.delete("/todo/{todo_id}", status_code=status.HTTP_204_NO_CONTENT)
# async def delete_todo(user: user_dependency, db: db_dependency, todo_id: int = Path(gt=0)):
#     check_user_authentication(user)
#
#     todo_model = db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get('id')).first()
#     if todo_model is None:
#         raise HTTPException(status_code=404, detail='Todo not found')
#     db.query(Todos).filter(Todos.id == todo_id).filter(Todos.owner_id == user.get('id')).delete()
#
#     db.commit()