from sentence_transformers import SentenceTransformer
from keybert import KeyBERT
from spacy.lang.ru import Russian

# Модель для эмбедингов
sbert_model = SentenceTransformer('sentence-transformers/Paraphrase-multilingual-MiniLM-L12-v2')
kw_model = KeyBERT(sbert_model)

# берём стоп-слова из spaCy для русского
stop_words = list(Russian().Defaults.stop_words)

def get_document_embedding(text: str) -> list[float]:
    # Возвращаем эмбединг документа
    return sbert_model.encode(text).tolist()

def extract_keywords(text: str, top_n: int = 10) -> list[tuple[str, float]]:
    # Возвращаем top_n ключевых фраз и их score.
    return kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=(1, 2),
        stop_words=stop_words,
        top_n=top_n
    )

if __name__ == "__main__":
    sample = "Машинное обучение - это область искусственного интеллекта, изучающая методы обучения моделей."
    print("Embedding length:", len(get_document_embedding(sample)))
    print("Keywords:", extract_keywords(sample))