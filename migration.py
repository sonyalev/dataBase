from models import Base

def migrate(engine):
    Base.metadata.create_all(engine)

