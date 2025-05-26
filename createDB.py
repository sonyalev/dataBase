import psycopg2


def create_database_PostgreSQL():

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


