import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def connect_db():

    conn = psycopg2.connect("dbname=bdlab3 user=postgres password=admin")
    cursor = conn.cursor()

    # об'єкт engine, який підключається до файлової бази даних
    engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/bdlab3', echo=True)
    Session = sessionmaker(bind=engine)

    return conn, cursor, engine, Session