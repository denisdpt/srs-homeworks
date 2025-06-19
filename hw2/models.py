from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey
from sqlalchemy.dialects.sqlite import JSON
from sqlalchemy.orm import relationship
#from hw2.database import Base
from database import Base

class Article(Base):
    __tablename__ = "articles"
    id        = Column(Integer, primary_key=True, index=True)
    url       = Column(String, unique=True, nullable=False)
    title     = Column(String, nullable=True)
    text      = Column(Text, nullable=False)
    embedding = Column(JSON, nullable=False)

    entities  = relationship("Entity", back_populates="article", cascade="all, delete")
    keywords  = relationship("Keyword", back_populates="article", cascade="all, delete")

class Entity(Base):
    __tablename__ = "entities"
    id         = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=False)
    text       = Column(String, nullable=False)
    label      = Column(String, nullable=False)

    article    = relationship("Article", back_populates="entities")

class Keyword(Base):
    __tablename__ = "keywords"
    id         = Column(Integer, primary_key=True, index=True)
    article_id = Column(Integer, ForeignKey("articles.id"), nullable=False)
    phrase     = Column(String, nullable=False)
    score      = Column(Float, nullable=False)

    article    = relationship("Article", back_populates="keywords")
