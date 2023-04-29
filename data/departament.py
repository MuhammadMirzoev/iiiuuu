from sqlalchemy import Column, Integer, String
from .db_session import DeclarativeBase


class Departament(DeclarativeBase):
    __tablename__ = 'departament'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=True)

    def __repr__(self):
        return f"{self.id}::{self.name}"
