from sqlalchemy import Column, Integer, String
from .db_session import DeclarativeBase


class Exponents(DeclarativeBase):
    __tablename__ = 'exponents'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column('name', String, nullable=True)
    region = Column('region', String)
    description = Column('description', String, nullable=True)
    link = Column('url', String)
    #
    # def __repr__(self):
    #     return f'{self.name}::{self.region}::{self.description}'

    # def get_all(self):
    #     return [self.name, self.region, self.description]
