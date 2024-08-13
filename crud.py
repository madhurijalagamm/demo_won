from sqlalchemy.orm import Session
import model
from schemas import UserCreate
def create_user(db: Session, name: str, email: str):
    db_user = model.User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
def get_user(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()
def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(model.User).offset(skip).limit(limit).all()
def update_user(db: Session, user_id: int, user_update: UserCreate):
    db_user = db.query(model.User).filter(model.User.id == user_id).first()
    if db_user:
        db_user.name = user_update.name
        db_user.email = user_update.email
        db.commit()
        db.refresh(db_user)
        return db_user
    return None
def delete_user(db: Session, user_id: int):
    db_user = db.query(model.User).filter(model.User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user
    return None
