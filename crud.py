from sqlalchemy.orm import Session
from models import Quote
from fastapi import HTTPException


def get_quotes(db: Session, author, page: int = 1, size: int = 6):
    offset = (page-1)*size

    query = db.query(Quote)
    if author:
        query = query.filter(Quote.author_name.ilike(f'{author}%'))

    total_items = query.count()
    quotes = query.offset(offset).limit(size).all()

    return {
        'data': {
            'quotes': quotes,
            'total_items': total_items
        }
    }


def create_quote(db: Session, author: str, quote: str):
    quote = Quote(author_name=author, quote=quote)

    db.add(quote)
    db.commit()
    db.refresh(quote)

    return {
        'data': {
            'quote': quote,
        }
    }


def get_quote(db: Session, quote_id: int):
    quote = db.query(Quote).filter_by(id=quote_id).first()
    if not quote:
        return HTTPException(status_code=404, detail='Quote not found')

    return {
        'data': {
            'quote': quote,
        }
    }
