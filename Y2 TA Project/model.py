from sqlalchemy import Column, Integer, String, Date, ForeignKey, Float, Boolean, DateTime
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Users(Base):
   __tablename__ = 'Users'
   id = Column(Integer, primary_key=True)
   username = Column(String)
   password = Column(String)
   
class Reviews(Base):
   __tablename__ = 'Reviews'
   id = Column(Integer, primary_key=True)
   name = Column(String)
   allergy= Column(String)
   review=Column(String)


