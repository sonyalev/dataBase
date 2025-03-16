import psycopg2
import threading
import time
import random

start_time = time.time()
random_user_id = random.randint(1, 100000)
print(random_user_id)

def optimistic_concurrency_control():
    conn = psycopg2.connect("dbname=bd_lab_2 user=postgres password=admin")
    cursor = conn.cursor()

    for _ in range(10000):
        while True:
            cursor.execute("SELECT counter, version FROM user_counter WHERE user_id = %s", (random_user_id, ))
            (counter, version) = cursor.fetchone()
            counter = counter + 1
            cursor.execute("UPDATE user_counter SET counter = %s, version = %s WHERE user_id = %s and version = %s", (counter, version + 1, random_user_id, version))

            conn.commit()
            count = cursor.rowcount
            if (count > 0):
                break

    cursor.close()
    conn.close()

threads = [threading.Thread(target=optimistic_concurrency_control) for _ in range(10)]

for thread in threads:
    thread.start()
for thread in threads:
    thread.join()
print("--- %s seconds ---" % (time.time() - start_time))
