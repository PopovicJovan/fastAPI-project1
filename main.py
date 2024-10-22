from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud
from database import engine, get_db
import models
from typing import Optional

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.post("/quotes")
async def create_quote(author_id: int, quote: str, db: Session = Depends(get_db)):
    return crud.create_quote(db=db, author_id=author_id, quote=quote)


@app.get("/quotes")
async def get_quotes(page: int, author_name: Optional[str] = None, db: Session = Depends(get_db)):
    return crud.get_quotes(db=db, author_name=author_name, page=page)


@app.get("/quotes/{quote_id}")
async def get_quote(quote_id: int, db: Session = Depends(get_db)):
    return crud.get_quote(db=db, quote_id=quote_id)


@app.post("/authors")
async def create_author(author_name: str, db: Session = Depends(get_db)):
    return crud.create_author(db=db, author_name=author_name)


@app.get("/authors")
async def get_authors(page: int, author_name: Optional[str] = None, db: Session = Depends(get_db)):
    return crud.get_authors(db=db, author_name=author_name, page=page)


@app.get("/authors/{author_id}")
async def get_author(author_id: int, db: Session = Depends(get_db)):
    return crud.get_author(db=db, author_id=author_id)
