from sqlalchemy import Column, Integer, String, Boolean, DateTime, Date, Numeric
from sqlalchemy.ext.declarative import declarative_base
import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    created = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
    username = Column(String(50))
    org_id = Column(Integer)
    first_name = Column(String(50))
    middle_name = Column(String(50))
    last_name = Column(String(50))
    sex = Column(String(10))
    birthdate = Column(Date)
    height = Column(Numeric)
    status = Column(String(20))
    password_hash = Column(String(200))
    role_name = Column(String(50))
    deleted = Column(Boolean)
    urgent_inspection = Column(Boolean)

    def __repr__(self):
        return f"<User(id={self.id}, username={self.username})>"