from sqlalchemy import Column, String, Integer, Float, Enum, Date, Time, ForeignKey, Boolean
import enum
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()
class WindDirection(enum.Enum):
    N = "N"
    NNW = "NNW"
    NE = "NE"
    E = "E"
    SE = "SE"
    SSE = "SSE"
    ESE = "ESE"
    NNE = "NNE"
    S = "S"
    WSW = "WSW"
    SSW = "SSW"
    SW = "SW"
    ENE = "ENE"
    W = "W"
    NW = "NW"
    WNW = "WNW"


class AirQuality(Base):
    __tablename__ = "air_quality"

    id = Column(Integer, primary_key=True)
    air_quality_carbon_monoxide = Column(Float)
    air_quality_ozone = Column(Float)
    air_quality_nitrogen_dioxide = Column(Float)
    air_quality_sulphur_dioxide = Column(Float)
    air_quality_pm2_5 = Column(Float)
    air_quality_pm10 = Column(Float)
    air_quality_us_epa_index = Column(Integer)
    air_quality_gb_defra_index = Column(Integer)
    going_outside = Column(Boolean)





class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    country = Column(String)
    wind_degree = Column(Integer)
    wind_kph = Column(Float)
    wind_direction = Column(Enum(WindDirection))
    last_updated = Column(Date)
    sunrise = Column(Time)


    #зовнішній ключ до таблиці air_quality
    air_quality_id = Column(Integer, ForeignKey("air_quality.id"))

    #встановлення зв'язку з таблицею air_quality
    air_quality = relationship("AirQuality")