import psycopg2


def set_value():
    conn = psycopg2.connect("dbname=bd_lab_2 user=postgres password=admin")
    cursor = conn.cursor()


    cursor.execute("UPDATE user_counter SET counter = 1")
    cursor.execute("UPDATE user_counter SET version = 0")
    conn.commit()

    print("Counter value 0")



    cursor.close()
    conn.close()

set_value()
