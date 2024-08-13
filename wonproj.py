import sqlalchemy
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
df = pd.read_csv('usagedb_crm_proposal.csv')
DATABASE_URL = "postgresql+psycopg2://postgres:admin123@localhost:5432/"
engine = create_engine(DATABASE_URL)
df.to_sql('crm.proposal', engine, if_exists='replace', index=False)
SessionLocal = sessionmaker(engine)
Base: DeclarativeMeta = sqlalchemy.orm.declarative_base()



