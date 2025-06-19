import sys
from database import Base, engine
from service import process_and_persist

def init_db():
    Base.metadata.create_all(bind=engine) # Создаём таблицы

if __name__ == "__main__":
    init_db()
    if len(sys.argv) < 2:
        print("Usage: python main.py <url1> [<url2> ...]")
        sys.exit(1)

    for url in sys.argv[1:]:
        try:
            process_and_persist(url)
        except Exception as e:
            print(f"Ошибка обработки {url}: {e}")
