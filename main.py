from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from wonproj import engine, SessionLocal
import model, crud
from schemas import Proposal, ProposalCreate, ProposalUpdate
# Create database tables
model.Base.metadata.create_all(bind=engine)
app = FastAPI()
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
@app.post("/proposals/", response_model=Proposal)
def create_proposal(proposal: ProposalCreate, db: Session = Depends(get_db)):
    return crud.create_proposal(db=db, proposal_create=proposal)

@app.get("/proposals/{proposal_id}", response_model=Proposal)
def read_proposal(proposal_id: str, db: Session = Depends(get_db)):
    db_proposal = crud.get_proposal(db, proposal_id=proposal_id)
    if db_proposal is None:
        raise HTTPException(status_code=404, detail="Proposal not found")
    return db_proposal
@app.put("/proposals/{proposal_id}", response_model=Proposal)
def update_proposal(proposal_id: str, proposal_update: ProposalUpdate, db: Session = Depends(get_db)):
    db_proposal = crud.update_proposal(db, proposal_id=proposal_id, proposal_update=proposal_update)
    if db_proposal is None:
        raise HTTPException(status_code=404, detail="Proposal not found")
    return db_proposal
@app.delete("/proposals/{proposal_id}", response_model=Proposal)
def delete_proposal(proposalid: str, db: Session = Depends(get_db)):
    db_proposal = crud.delete_proposal(db, proposalid=proposalid)
    if db_proposal is None:
        raise HTTPException(status_code=404, detail="Proposal not found")
    return db_proposal
