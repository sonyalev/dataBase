from models import Base

def create_table(engine):
    Base.metadata.create_all(engine)

