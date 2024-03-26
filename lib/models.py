# models.py

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Student(Base):
    __tablename__ = 'students'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    # Add more columns as needed

    # Rename a column
    renamed_column = Column('new_name', String)
