import re
from connectDB import connect_db
from migration import run_flyway_migrations
from models import Weather, AirQuality


def find_weather_info(session):
    """Функція для пошуку погоди за країною та датою."""
    while True:
        country_input = input("Введіть країну: ").strip()
        if country_input:
            break
        else:
            print("Не правильно введені дані")

    while True:
        date_input = input("Введіть дату у форматі YYYY-MM-DD: ").strip()
        if re.match(r'\d{4}-\d{2}-\d{2}', date_input):
            break
        else:
            print("Не правильно введені дані. Введіть дату у форматі YYYY-MM-DD")


    weather_info = session.query(Weather).join(AirQuality, AirQuality.weather_id == Weather.id).filter(
        Weather.country == country_input,
        Weather.last_updated == date_input
    ).first()

    if weather_info:
        print("\n------------------------------------------------------------\n")
        print(f"\nWether in {weather_info.country} on {weather_info.last_updated}:")
        print(f" wind_degree: {weather_info.wind_degree}")
        print(f" wind_kph: {weather_info.wind_kph}")
        print(f" wind_direction: {weather_info.wind_direction.name}")
        print(f" sunrise: {weather_info.sunrise}")
        print("\n------------------------------------------------------------\n")


        if weather_info.air_quality:
            print("\n------------------------------------------------------------\n")
            print("\nСтан повітря:")
            print(f" air_quality_carbon_monoxide: {weather_info.air_quality.air_quality_carbon_monoxide}")
            print(f" air_quality_ozone: {weather_info.air_quality.air_quality_ozone}")
            print(f" air_quality_nitrogen_dioxide: {weather_info.air_quality.air_quality_nitrogen_dioxide}")
            print(f" air_quality_sulphur_dioxide: {weather_info.air_quality.air_quality_sulphur_dioxide}")
            print(f" air_quality_pm2_5: {weather_info.air_quality.air_quality_pm2_5}")
            print(f" air_quality_pm10: {weather_info.air_quality.air_quality_pm10}")
            print(f" air_quality_us_epa_index: {weather_info.air_quality.air_quality_us_epa_index}")
            print(f" air_quality_gb_defra_index: {weather_info.air_quality.air_quality_gb_defra_index}")
            print(f"  Чи варто виходити на вулицю: {'Так' if weather_info.air_quality.going_outside else 'Ні'}")
            print("\n------------------------------------------------------------\n")
        else:
            print("Дані про якість повітря відсутні")
    else:
        print("\nДані не знайдено для вказаної країни та дати")



def main():

    #create_database()

    #підключаємось до бази та отримуємо об'єкти
    conn, cursor, engine, Session = connect_db()


    # migrate(engine)
    #
    #
    # read_data(Session)

    run_flyway_migrations()

    session = Session()

    find_weather_info(session)

    session.close()


if __name__ == '__main__':
    main()