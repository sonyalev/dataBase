from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from models import Base
from connectDB import engine

meta = MetaData()

#створення таблиці
Base.metadata.create_all(engine)

