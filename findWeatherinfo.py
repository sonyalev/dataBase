from modelsAfterRefactoring import Weather, AirQuality
import re

def find_weather_info(session):
    """Функція для пошуку погоди за країною та датою."""
    # Введення назви країни
    while True:
        country_input = input("Введіть країну: ").strip()
        if country_input:
            break
        else:
            print("Не правильно введені дані")

    # Введення дати
    while True:
        date_input = input("Введіть дату у форматі YYYY-MM-DD: ").strip()
        if re.match(r'^\d{4}-\d{2}-\d{2}$', date_input):
            break
        else:
            print("Не правильно введені дані. Введіть дату у форматі YYYY-MM-DD")

    # Пошук даних про погоду
    weather_info = session.query(Weather).join(AirQuality).filter(
        Weather.country == country_input,
        Weather.last_updated == date_input
    ).first()

    if weather_info:
        print("\n------------------------------------------------------------\n")
        print(f"Погода в {weather_info.country} на {weather_info.last_updated}:")
        print(f"  Швидкість вітру: {weather_info.wind_kph} км/год")
        print(f"  Напрям вітру: {weather_info.wind_direction.name}")
        print(f"  Час сходу сонця: {weather_info.sunrise}")
        print("\n------------------------------------------------------------\n")

        if weather_info.air_quality:
            print("Якість повітря:")
            for aq in weather_info.air_quality:
                print(f"  CO: {aq.air_quality_carbon_monoxide}")
                print(f"  Озон: {aq.air_quality_ozone}")
                print(f"  Діоксид азоту: {aq.air_quality_nitrogen_dioxide}")
                print(f"  Діоксид сірки: {aq.air_quality_sulphur_dioxide}")
                print(f"  PM2.5: {aq.air_quality_pm2_5}")
                print(f"  PM10: {aq.air_quality_pm10}")
                print(f"  Індекс US EPA: {aq.air_quality_us_epa_index}")
                print(f"  Індекс GB DEFRA: {aq.air_quality_gb_defra_index}")
                print(f"  Чи варто виходити на вулицю: {'Так' if aq.going_outside else 'Ні'}")
                print("\n------------------------------------------------------------\n")
        else:
            print("Дані про якість повітря відсутні\n")
    else:
        print("\nДані не знайдено для вказаної країни та дати")