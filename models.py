from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from database import Base


class Quote(Base):
    __tablename__ = "quotes"
    id = Column(Integer, primary_key=True)
    author_id = Column(Integer, ForeignKey("authors.id"))
    quote = Column(Text)

    author = relationship("Author", back_populates="quotes")


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    quotes = relationship("Quote", back_populates="author")
