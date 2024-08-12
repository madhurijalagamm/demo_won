import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm import sessionmaker
DATABASE_URL = "postgresql+psycopg2://postgres:admin123@localhost:5432/"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(engine)
Base: DeclarativeMeta = sqlalchemy.orm.declarative_base()
