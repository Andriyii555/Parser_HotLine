from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import mapper
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Text, String, Float


Base = declarative_base()
class HotLine(Base):
    __tablename__ = 'offer'

    id = Column(Integer, primary_key=True)
    ref = Column(String)
    offer_count = Column(String)


    def __init__(self, ref, offer_count):
        self.ref = ref
        self.offer_count = offer_count

db_engine = create_engine("sqlite:///HotLine.db", echo=True)
Base.metadata.create_all(db_engine)

