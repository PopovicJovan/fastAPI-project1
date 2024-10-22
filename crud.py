from sqlalchemy.orm import Session
from models import Quote, Author
from fastapi import HTTPException
from typing import Dict, Any

# Quotes crud
def get_quotes(db: Session, author_name: str = "", page: int = 1, size: int = 6) -> Dict[str, Any]:
    offset = (page-1)*size

    query = db.query(Quote)
    if author_name:
        query = query.join(Author).filter(Author.name.ilike(f'{author_name}%'))

    total_items = query.count()
    quotes = query.offset(offset).limit(size).all()

    return {
        'data': {
            'quotes': quotes,
            'total_items': total_items
        }
    }


def create_quote(db: Session, author_id: int, quote: str) -> Dict[str, Any]:
    quote = Quote(author_id=author_id, quote=quote)

    db.add(quote)
    db.commit()
    db.refresh(quote)

    return {
        'data': {
            'quote': quote,
        }
    }


def get_quote(db: Session, quote_id: int) -> Dict[str, Any] | HTTPException:
    quote = db.query(Quote).filter_by(id=quote_id).first()
    if not quote:
        return HTTPException(status_code=404, detail='Quote not found')

    return {
        'data': {
            'quote': quote
        }
    }


# Authors crud
def get_authors(db: Session, author_name: str = "", page: int = 1, size: int = 6) -> Dict[str, Any]:
    offset = (page-1)*size

    query = db.query(Author)
    if author_name:
        query = query.filter(Author.name.ilike(f'{author_name}%'))

    total_items = query.count()
    authors = query.offset(offset).limit(size).all()

    return {
        'data': {
            'author': authors,
            'total_items': total_items
        }
    }

def get_author(db: Session, author_id: int) -> Dict[str, Any] | HTTPException:
    author = db.query(Author).filter_by(id=author_id).first()
    if not author:
        return HTTPException(status_code=404, detail='Author not found')

    return {
        'data': {
            'author': author
        }
    }


def create_author(db: Session, author_name: str) -> Dict[str, Any]:
    author = Author(name=author_name)

    db.add(author)
    db.commit()
    db.refresh(author)

    return {
        'data': {
            'author': author,
        }
    }