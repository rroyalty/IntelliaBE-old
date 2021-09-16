from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import JSON
from ..database import Base


class Lessons(Base):
    __tablename__ = "Lessons"

    id = Column(Integer, primary_key=True, nullable=False)
    department = Column(String(30), nullable=False)
    course = Column(String(30), nullable=False)
    subject = Column(String(30), nullable=False)
    name = Column(String(30), nullable=False)
    description = Column(String(255))
    instructions = Column(JSON)
    tier = Column(String(20), nullable=False) #Elementary, Middle, High
    grade = Column(String(2), nullable=False) #K-12
    created_by = Column(String(30), nullable=False)
