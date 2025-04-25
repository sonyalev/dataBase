from sqlalchemy import Column, String, Integer, Float, Enum, Date, Time
from sqlalchemy.ext.declarative import declarative_base
import enum
from sqlalchemy.orm import declarative_base
# 3 етап моделі

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

class Weather(Base):
    __tablename__ = 'weather'

    id = Column(Integer, primary_key=True)
    country = Column(String)
    wind_degree = Column(Integer)
    wind_kph = Column(Float)
    wind_direction = Column(Enum(WindDirection))
    last_updated = Column(Date)
    sunrise = Column(Time)
    air_quality_Carbon_Monoxide = Column(Float)
    air_quality_Ozone = Column(Float)
    air_quality_Nitrogen_dioxide = Column(Float)
    air_quality_Sulphur_dioxide = Column(Float)
    air_quality_PM2_5 = Column(Float)
    air_quality_PM10 = Column(Float)
    air_quality_us_epa_index = Column(Integer)
    air_quality_gb_defra_index = Column(Integer)


