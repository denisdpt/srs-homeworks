import os, sys
ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, ROOT)

import json, re
from collections import defaultdict
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from hw2.models import Article, Keyword
from hw2.database import Base
from sqlalchemy.exc import NoResultFound

DATABASE_URL = "sqlite:///../hw2/articles.db"
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
Session = sessionmaker(bind=engine)

def load_roadmap(path="roadmap.json"):
    with open(path, encoding="utf-8") as f:
        return json.load(f)

def save_matched_roadmap(data, path="matched_roadmap.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def collect_article_keywords(session):
    kws = defaultdict(list)
    urls = {}
    for kw in session.query(Keyword).all():
        kws[kw.article_id].append(kw.phrase.lower())
    for art in session.query(Article.id, Article.url):
        urls[art.id] = art.url
    return kws, urls

def match_topics_substring(roadmap, article_kws, article_urls):
    #Для каждой темы разбиваем её ключевые слова на отдельные слова, и ищем, содержится ли какое-нибудь из них в ключевых фразах статьи.
    word_split = re.compile(r'\w+', re.UNICODE)
    for topic in roadmap["topics"]:
        # получим уникальные слова темы
        topic_words = set()
        for phrase in topic["keywords"]:
            for w in word_split.findall(phrase.lower()):
                if len(w) > 2:    # коротыши-стопы выкидываем
                    topic_words.add(w)
        matched = set()
        for aid, phrases in article_kws.items():
            for art_phrase in phrases:
                for w in topic_words:
                    if w in art_phrase:
                        matched.add(article_urls[aid])
                        break
                if aid in matched:
                    break

        topic["articles"] = list(matched)
    return roadmap

def main():
    roadmap = load_roadmap("../hw3/roadmap.json")
    session = Session()
    article_kws, article_urls = collect_article_keywords(session)
    session.close()

    matched = match_topics_substring(roadmap, article_kws, article_urls)
    save_matched_roadmap(matched)

    # отчёт для тем
    for topic in matched["topics"]:
        print(f"[{topic['id']}] {topic['title']}")
        if topic["articles"]:
            for url in topic["articles"]:
                print("  •", url)
        else:
            print("  - нет статей")
        print()

if __name__ == "__main__":
    main()
