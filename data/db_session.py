import sqlalchemy as sa
from sqlalchemy.orm import Session
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DeclarativeBase = declarative_base()  # Экспорт в таблицы

__factory = None





def global_init():
    global __factory

    if __factory:
        return
    conn_str = f'postgresql+psycopg2://vystavka_user:Vystavka23@192.168.88.201/vystavka'
    print(f"Подключение к базе данных по адресу {conn_str}")

    engine = sa.create_engine(conn_str, echo=False)
    DeclarativeBase.metadata.create_all(engine)
    __factory = sessionmaker(bind=engine)

    # noinspection PyUnresolvedReferences
    from . import __all_models


def create_session() -> Session:
    global __factory
    return __factory()
