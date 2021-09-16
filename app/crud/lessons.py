from typing import List, TypeVar

from sqlalchemy.orm import Session
from fastapi.encoders import jsonable_encoder

from ..models.lessons import Lessons, Base
from ..schemas.lessons import BaseModel

ModelType = TypeVar("ModelType", bound=Base)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)

def get_lesson_by_name(session: Session, name: str) -> ModelType:
    return session.query(Lessons).filter(Lessons.name == name).first()

def get_lessons(session: Session) -> List[ModelType]:
    return session.query(Lessons).all()

def add_lesson(obj_in: CreateSchemaType, session: Session) -> ModelType:
    obj_in_data = jsonable_encoder(obj_in)
    obj_db = Lessons(**obj_in_data)
    session.add(obj_db)
    session.commit()
    session.refresh(obj_db)
    return obj_db