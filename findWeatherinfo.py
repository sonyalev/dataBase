from modelsAfterRefactoring import Weather, AirQuality
import re

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


    weather_info = session.query(Weather).join(AirQuality, AirQuality.id == Weather.id).filter(
        Weather.country == country_input,
        Weather.last_updated == date_input
    ).first()

    if weather_info:
        print("\n------------------------------------------------------------\n")
        print(f"\nПогода в {weather_info.country} на {weather_info.last_updated}:")
        print(f"  Швидкість вітру: {weather_info.wind_kph} км/год")
        print(f"  Напрям вітру: {weather_info.wind_direction.name}")
        print(f"  Час сходу сонця: {weather_info.sunrise}")
        print("\n------------------------------------------------------------\n")


        if weather_info.air_quality:
            print("\n------------------------------------------------------------\n")
            print("\nЯкість повітря:")
            print(f"  CO: {weather_info.air_quality.air_quality_carbon_monoxide}")
            print(f"  Озон: {weather_info.air_quality.air_quality_ozone}")
            print(f"  Чи варто виходити на вулицю: {'Так' if weather_info.air_quality.going_outside else 'Ні'}")
            print("\n------------------------------------------------------------\n")
        else:
            print("Дані про якість повітря відсутні")
    else:
        print("\nДані не знайдено для вказаної країни та дати")