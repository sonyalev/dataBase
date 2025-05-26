import re
from Demos.win32ts_logoff_disconnected import session
from sqlalchemy import Table, MetaData, inspect, select, text
from connectDB import connect_db_PostgreSQL
from findWeatherinfo import find_weather_info
from migration import run_flyway_migrations
from modelsAfterRefactoring import Weather, AirQuality
from sqlalchemy.orm import sessionmaker





def main():

    #create_database()

    #підключаємось до бази та отримуємо об'єкти
    conn, cursor, engine, Session = connect_db_PostgreSQL()


    # create_table(engine)

    # read_data(Session)

    # run_flyway_migrations()

    session = Session()

    find_weather_info(session)

    session.close()


if __name__ == '__main__':
    main()