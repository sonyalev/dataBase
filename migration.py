from models import Base, Weather
import subprocess
def create_table(engine):
    Base.metadata.create_all(engine)

def run_flyway_migrations():
    """Запускає Flyway міграції."""
    try:
        subprocess.run([r"C:\Program Files\Red Gate\Flyway Desktop\flyway.cmd", "baseline"], check=True)
        subprocess.run([r"C:\Program Files\Red Gate\Flyway Desktop\flyway.cmd", "migrate"], check=True)
        print("Міграції виконано")
    except subprocess.CalledProcessError as e:
        print(f"Помилка при виконанні: {e}")




