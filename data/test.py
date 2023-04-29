from sqlalchemy import create_engine


engine = create_engine()

print(engine.echo)
import psycopg2 as pgsql
from psycopg2 import OperationalError
try:
    connection = pgsql.connect(database='test_db', user='db_user', password='yourPassword', host='localhost', port='5432')
    print('<h2>Подключение к базе данных выполнено успешно</h2>')
    connection.close()
except OperationalError as error:
    print(f'<h2>Ошибка подключения к БД: {error} </h2>')