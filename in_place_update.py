import psycopg2
import threading
import time
import random

start_time = time.time()
random_user_id = random.randint(1, 100000)
print(random_user_id)

def in_place_update():
    conn = psycopg2.connect("dbname=bd_lab_2 user=postgres password=admin")
    cursor = conn.cursor()

    for _ in range(10000):
        cursor.execute("UPDATE user_counter SET counter = counter + 1 WHERE user_id = %s", (random_user_id,))
        conn.commit()

    cursor.close()
    conn.close()

threads = [threading.Thread(target=in_place_update) for _ in range(10)]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("--- %s seconds ---" % (time.time() - start_time))