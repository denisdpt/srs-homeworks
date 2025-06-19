import sys
from fetcher import fetch_article_text
from ner import extract_entities
from embedding import get_document_embedding, extract_keywords

def process_article(url: str):
    # 1) скачиваем текст
    text = fetch_article_text(url)
    # 2) именованные сущности
    entities = extract_entities(text)
    print("Named Entities:", entities)
    # 3) эмбединг документа
    embedding = get_document_embedding(text)
    print("Embedding size:", len(embedding))
    # 4) ключевые слова
    keywords = extract_keywords(text, top_n=10)
    print("Keywords:", keywords)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <article_url>")
        sys.exit(1)
    process_article(sys.argv[1])
