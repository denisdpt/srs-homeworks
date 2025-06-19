#from hw2.database import SessionLocal
#from hw2.repository import save_article, save_entities, save_keywords
from database import SessionLocal
from repository import save_article, save_entities, save_keywords
from fetcher import fetch_article
from ner import extract_entities
from embedding import get_document_embedding, extract_keywords

def process_and_persist(url: str):
    # 1) Парсим статью
    title, text = fetch_article(url)

    # 2) Извлекаем NER, эмбединг и ключевые слова
    entities  = extract_entities(text)
    embedding = get_document_embedding(text)
    keywords  = extract_keywords(text)

    # 3) Сохраняем в БД
    session = SessionLocal()
    art = save_article(session, url, title, text, embedding)
    save_entities(session, art.id, entities)
    save_keywords(session, art.id, keywords)
    session.close()

    print(f"Данные сохранены для {url}")
