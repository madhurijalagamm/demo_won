from sqlalchemy.orm import Session
import model
def get_user(db: Session, user_id: int):
    return db.query(model.User).filter(model.User.id == user_id).first()

def create_user(db: Session, name: str, email: str):
    db_user = model.User(name=name, email=email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
