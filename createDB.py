import psycopg2

# 1 етап -  створення бази даних

#підключення до PostgreSQL
conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)

#створюємо
conn.autocommit = True
cursor = conn.cursor()
cursor.execute("CREATE DATABASE bdlab3")

#закриваємо з'єднання до старої бази даних
cursor.close()
conn.close()


