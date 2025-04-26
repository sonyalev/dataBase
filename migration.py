from models import Base
import subprocess

def migrate(engine):
    Base.metadata.create_all(engine)



def run_flyway_migrations():
    """Запускає Flyway міграції."""
    try:
        # Спочатку baseline (якщо потрібно)
        subprocess.run([r"C:\Users\sofia\flyway\flyway.cmd", "baseline"], check=True)
        print("Baseline виконано")

        # Потім migrate
        subprocess.run([r"C:\Users\sofia\flyway\flyway.cmd", "migrate"], check=True)
        print("Міграції виконано")
    except subprocess.CalledProcessError as e:
        print(f"Помилка при виконанні: {e}")
    except subprocess.CalledProcessError as e:
        print(f"Помилка при виконанні міграцій: {e}")
