from connectDB import connect_db
from readData import read_data
from createDB import create_database
from migration import migrate

def main():

    #create_database()

    #підключаємось до бази та отримуємо об'єкти
    conn, cursor, engine, Session = connect_db()


    # migrate(engine)
    #
    #
    # read_data(Session)


if __name__ == '__main__':
    main()