from connectDB import connect_db, connect_MySQLdb
from migration import run_flyway_migrations, create_table
from models import Weather, Base
from readData import read_data








def main():

    #підключаємось до бази та отримуємо об'єкти
    conn, cursor, engine, Session = connect_MySQLdb()


    create_table(engine)

    read_data(Session)

    run_flyway_migrations()









if __name__ == '__main__':
    main()