import psycopg2
import threading
import time
import random

start_time = time.time()
random_user_id = random.randint(1, 100000)
print(random_user_id)

def row_level_locking():
    conn = psycopg2.connect("dbname=bd_lab_2 user=postgres password=admin")
    cursor = conn.cursor()

    for _ in range(10000):
        cursor.execute("SELECT counter FROM user_counter WHERE user_id = %s FOR UPDATE", (random_user_id, ))
        counter = cursor.fetchone()[0] + 1
        cursor.execute("UPDATE user_counter SET counter = %s WHERE user_id = %s", (counter, random_user_id))
        conn.commit()

    cursor.close()
    conn.close()

threads = [threading.Thread(target=row_level_locking) for _ in range(10)]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("--- %s seconds ---" % (time.time() - start_time))