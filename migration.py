from models import Base
import subprocess

def migrate(engine):
    Base.metadata.create_all(engine)




