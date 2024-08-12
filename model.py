from sqlalchemy import Column, Integer, String
# from .database import Base
from wonproj import Base
class User(Base):
    __tablename__ = "employee"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)

