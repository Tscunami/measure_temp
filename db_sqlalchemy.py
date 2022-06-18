"""Db file"""

import sqlalchemy
from sqlalchemy import MetaData
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base

DB_NAME = "temperatures.db"

engine = sqlalchemy.create_engine(f'sqlite:///{DB_NAME}', future=True)

Base = declarative_base()


class Temperature(Base):
    """Temperature at current time"""

    __tablename__ = "temperatures"
    id = Column(Integer, primary_key=True)
    temperature = Column(String)
    created_at = Column(DateTime)


Base.metadata.create_all(engine)

# to be able to reflect tables
meta_data = MetaData(bind=engine)
MetaData.reflect(meta_data)