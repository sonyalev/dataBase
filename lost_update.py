import psycopg2
import threading   # для роботи із потоками
import time
import random

start_time = time.time()

random_user_id = random.randint(1, 100000)
print(random_user_id)

def lost_update():
    conn = psycopg2.connect("dbname=bd_lab_2 user=postgres password=admin")
    cursor = conn.cursor()

    for _ in range(10000):

        cursor.execute("SELECT counter FROM user_counter WHERE user_id = %s", (random_user_id,))
        counter = cursor.fetchone()[0] + 1                        #cursor.fetchone() повертає один рядок результату у вигляді кортежу (tuple)
        cursor.execute("UPDATE user_counter SET counter = %s WHERE user_id = %s", (counter, random_user_id))
        conn.commit()



    cursor.close()
    conn.close()

threads = [threading.Thread(target=lost_update) for _ in range(10)]

for thread in threads:
    thread.start()
for thread in threads:  #гарантує, що головний потік буде чекати завершення всіх потоків перед виконанням наступних команд.
    thread.join()

print("--- %s seconds ---" % (time.time() - start_time))