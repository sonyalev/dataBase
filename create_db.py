import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)

cursor = conn.cursor()

cursor.execute("CREATE DATABASE bd_lab_2")

# Закриваємо з'єднання до старої бази даних
cursor.close()
conn.close()

conn = psycopg2.connect("dbname=bd_lab_2 user=postgres password=admin")
cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE user_counter (
        user_id SERIAL PRIMARY KEY,
        counter INTEGER,
        version INTEGER)
""")

cursor.execute("INSERT INTO user_counter (counter, version) VALUES (%s, %s)", (1, 0))

# 3. Заповнити таблицю 100000 рядками
for i in range(1, 100001):
    cursor.execute("INSERT INTO user_counter (user_id, counter, version) VALUES (%s, %s, %s)", (i, 1, 0))

conn.commit()
cursor.close()
conn.close()








