import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

import pymysql

def connect_db_PostgreSQL():

    conn = psycopg2.connect("dbname=bdlab3 user=postgres password=admin")
    cursor = conn.cursor()

    # об'єкт engine, який підключається до файлової бази даних
    engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/bdlab3', echo=True)
    Session = sessionmaker(bind=engine)

    return conn, cursor, engine, Session



def connect_MySQLdb():

    conn = pymysql.connect(
        host="localhost",
        user="root",
        password="admin",
        database="bdlab3"
    )
    cursor = conn.cursor()

    engine = create_engine('mysql+pymysql://root:admin@localhost:3306/bdlab3', echo=True)

    Session = sessionmaker(bind=engine)

    return conn, cursor, engine, Session
