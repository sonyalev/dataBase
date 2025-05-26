from connectDB import connect_db_PostgreSQL
from readData import read_data
from createDB import create_database
from migration import create_table, run_flyway_migrations


def main():

    # create_database()

    # підключаємось до бази та отримуємо об'єкти
    conn, cursor, engine, Session = connect_db_PostgreSQL()

    # create_table(engine)

    # read_data(Session)

    run_flyway_migrations()

if __name__ == '__main__':
    main()