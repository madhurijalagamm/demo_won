from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from wonproj import engine, SessionLocal
import model, crud
from schemas import ProposalCreate, Proposal

# Create database tables
model.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Endpoint to create a proposal
@app.post("/proposals/", response_model=Proposal)
def create_proposal(proposal: ProposalCreate, db: Session = Depends(get_db)):
    return crud.create_proposal(db=db, **proposal.dict())

# Endpoint to read a proposal by ID
@app.get("/proposals/{proposal_id}", response_model=Proposal)
def read_proposal(proposal_id: str, db: Session = Depends(get_db)):
    db_proposal = crud.get_proposal(db, proposal_id=proposal_id)
    if db_proposal is None:
        raise HTTPException(status_code=404, detail="Proposal not found")
    return db_proposal
