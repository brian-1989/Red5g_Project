"""Food module.

"""
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class food(Base):
    __tablename__ = 'food_table'

    id = Column(Integer, nullable=False, autoincrement=True, primary_key=True)
    name = Column(String(30), nullable=False)
    value = Column(Integer, nullable=False)