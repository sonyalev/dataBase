import psycopg2
from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from sqlalchemy.orm import declarative_base, sessionmaker

# 2 етап

#підключаємося до новоствореної бази даних
conn = psycopg2.connect("dbname=bdlab3 user=postgres password=admin")
cursor = conn.cursor()

 #створює об'єкт engine, який підключається до файлової бази даних
engine = create_engine('postgresql+psycopg2://postgres:admin@localhost:5432/bdlab3', echo=True)
Session = sessionmaker(bind=engine)   # Готуєш "шаблон" сесій