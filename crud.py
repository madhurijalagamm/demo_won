from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from model import Proposal
Base = declarative_base()
def create_proposal(db: Session, proposal_create):
    db_proposal = Proposal(**proposal_create.dict())
    db.add(db_proposal)
    db.commit()
    db.refresh(db_proposal)
    return db_proposal
def get_proposal(db: Session, proposal_id: str):
    return db.query(Proposal).filter(Proposal.id == proposal_id).first()
def update_proposal(db: Session, proposal_id: str, proposal_update):
    db_proposal = db.query(Proposal).filter(Proposal.id == proposal_id).first()
    if db_proposal:
        for key, value in proposal_update.dict(exclude_unset=True).items():
            setattr(db_proposal, key, value)
        db.commit()
        db.refresh(db_proposal)
        return db_proposal
    return None

def delete_proposal(db: Session, proposalid: str):
    db_proposal = db.query(Proposal).filter(Proposal.id == proposalid).first()
    if db_proposal:
        db.delete(db_proposal)
        db.commit()
        return db_proposal
    return None
