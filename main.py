from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
import psycopg2
from sqlalchemy.orm import declarative_base, sessionmaker
from models import Base
from connectDB import engine

#4 етап
meta = MetaData()

#створення таблиці
Base.metadata.create_all(engine)

