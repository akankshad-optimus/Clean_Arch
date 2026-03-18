from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.db import get_db
from app.services import user_service
from pydantic import BaseModel

router = APIRouter(prefix="/api/users", tags=["users"])

class UserSchema(BaseModel):
    name: str
    email: str
    age: int

@router.post("/", status_code=201)
def create_user(user: UserSchema, db: Session = Depends(get_db)):
    return user_service.create_user(db, user)

@router.get("/")
def get_users(db: Session = Depends(get_db)):
    return user_service.get_users(db)

@router.put("/{user_id}")
def update_user(user_id: int, user: UserSchema, db: Session = Depends(get_db)):
    return user_service.update_user(db, user_id, user)

@router.delete("/{user_id}", status_code=204)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    user_service.delete_user(db, user_id)
    return {"detail": "deleted"}
