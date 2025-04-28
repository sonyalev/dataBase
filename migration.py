from models import Base, Weather, AirQuality

def migrate(engine):
    Base.metadata.create_all(engine)



def migrate_data(postgres_session, mysql_session):
    """Переносить дані з Postgres до MySQL."""

    try:

        weather_records = postgres_session.query(Weather).all()

        mysql_session.query(AirQuality).delete()
        mysql_session.query(Weather).delete()
        mysql_session.commit()

        for weather in weather_records:
            new_air_quality = AirQuality(
                air_quality_carbon_monoxide=weather.air_quality.air_quality_carbon_monoxide,
                weather_id=weather.air_quality.id,
                air_quality_ozone=weather.air_quality.air_quality_ozone,
                air_quality_nitrogen_dioxide=weather.air_quality.air_quality_nitrogen_dioxide,
                air_quality_sulphur_dioxide=weather.air_quality.air_quality_sulphur_dioxide,
                air_quality_pm2_5=weather.air_quality.air_quality_pm2_5,
                air_quality_pm10=weather.air_quality.air_quality_pm10,
                air_quality_us_epa_index=weather.air_quality.air_quality_us_epa_index,
                air_quality_gb_defra_index=weather.air_quality.air_quality_gb_defra_index,
                going_outside=bool(weather.air_quality.going_outside)
            )
            mysql_session.add(new_air_quality)
            mysql_session.flush()

            new_weather = Weather(
                country=weather.country,
                wind_degree=weather.wind_degree,
                wind_kph=weather.wind_kph,
                wind_direction=weather.wind_direction,
                last_updated=weather.last_updated,
                sunrise=weather.sunrise,
                air_quality_id=new_air_quality.id
            )
            mysql_session.add(new_weather)

        mysql_session.commit()
        print("Дані успішно перенесено до MySQL.")

    except Exception as e:
        mysql_session.rollback()
        print(f"Помилка при перенесенні даних: {e}")

    finally:

        postgres_session.close()
        mysql_session.close()


