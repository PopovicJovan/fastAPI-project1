from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
import crud
from database import engine, get_db
import models
from typing import Optional

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


@app.post("/quotes")
async def create_quote(author: str, quote: str, db: Session = Depends(get_db)):
    return crud.create_quote(db=db, author=author, quote=quote)


@app.get("/quotes")
async def get_quotes(author: Optional[str] = None, db: Session = Depends(get_db)):
    return crud.get_quotes(db=db, author=author)


@app.get("/quotes/{quote_id}")
async def get_quotes(quote_id: int, db: Session = Depends(get_db)):
    return crud.get_quote(db=db, quote_id=quote_id)
