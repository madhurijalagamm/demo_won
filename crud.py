from sqlalchemy.orm import Session
from model import Proposal  # Assuming the Proposal model is defined in the model module

def create_proposal(db: Session, **kwargs):
    db_proposal = Proposal(**kwargs)
    db.add(db_proposal)
    db.commit()
    db.refresh(db_proposal)
    return db_proposal

def get_proposal(db: Session, proposal_id: str):
    return db.query(Proposal).filter(Proposal.id == proposal_id).first()
