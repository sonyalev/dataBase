import pandas as pd
from models import Weather, WindDirection
from datetime import datetime

def read_data(Session):
    df = pd.read_csv("GlobalWeatherRepository.csv")
    session = Session()
    weather_objects = []

    for _, row in df.iterrows():
        weather = Weather(
            country=row['country'],
            wind_degree=int(row['wind_degree']),
            wind_kph=float(row['wind_kph']),
            wind_direction=WindDirection(row['wind_direction']),
            last_updated=pd.to_datetime(row['last_updated']),
            sunrise=datetime.strptime(row['sunrise'].strip(), "%I:%M %p").time(),
            air_quality_carbon_monoxide=float(row['air_quality_Carbon_Monoxide']),
            air_quality_ozone=float(row['air_quality_Ozone']),
            air_quality_nitrogen_dioxide=float(row['air_quality_Nitrogen_dioxide']),
            air_quality_sulphur_dioxide=float(row['air_quality_Sulphur_dioxide']),
            air_quality_pm2_5=float(row['air_quality_PM2.5']),
            air_quality_pm10=float(row['air_quality_PM10']),
            air_quality_us_epa_index=int(row['air_quality_us-epa-index']),
            air_quality_gb_defra_index=int(row['air_quality_gb-defra-index'])
        )
        weather_objects.append(weather)


    session.bulk_save_objects(weather_objects)
    session.commit()
