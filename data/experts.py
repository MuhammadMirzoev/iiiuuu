from sqlalchemy import Column, Integer, String
from .db_session import DeclarativeBase


class Experts(DeclarativeBase):
    __tablename__ = 'experts'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=True)
    media = Column('url', String)
    description = Column('description', String, nullable=True)
    departament = Column('departament', Integer, nullable=True)

    def __repr__(self):
        return f'{self.name}::{self.media}::{self.description}::{self.description}'