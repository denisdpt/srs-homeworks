from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
#from hw2.models import Article, Entity, Keyword
from models import Article, Entity, Keyword

def save_article(session: Session, url: str, title: str, text: str, embedding: list) -> Article:
    art = Article(
        url=url,
        title=title,
        text=text,
        embedding=embedding
    )
    session.add(art)
    try:
        session.commit()
    except IntegrityError:
        session.rollback()
        art = session.query(Article).filter(Article.url == url).one()
    return art

def save_entities(session: Session, article_id: int, entities: list[tuple[str, str]]):
    for text, label in entities:
        session.add(Entity(article_id=article_id, text=text, label=label))
    session.commit()

def save_keywords(session: Session, article_id: int, keywords: list[tuple[str, float]]):
    for phrase, score in keywords:
        session.add(Keyword(article_id=article_id, phrase=phrase, score=score))
    session.commit()
