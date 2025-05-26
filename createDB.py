import psycopg2
from sqlalchemy.dialects import mysql
#import mysql.connector

def create_database():

    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="admin",
        host="localhost",
        port="5432"
    )

    conn.autocommit = True
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE bdlab3")

    cursor.close()
    conn.close()


def create_database_MySQL():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="admin"
    )

    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS bdlab3")

    print("Базу даних 'bdlab3' створено (або вона вже існує).")

    cursor.close()
    conn.close()

