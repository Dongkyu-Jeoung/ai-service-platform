# =========================================================
# 도서 관리 어플리케이션
# =========================================================


from fastapi import APIRouter, Path, HTTPException, status, Depends
from schemas.book_schema import Book, BookInfo
from sqlalchemy import select, delete
from sqlalchemy.orm import Session
from database import get_db
from models.book_model import BookModel

router = APIRouter()

book_list = []

# C
@router.post("/", response_model = Book, status_code = status.HTTP_201_CREATED)
async def add_book(book : BookInfo, db : Session = Depends(get_db)) -> dict:
    new_book = BookModel(
        title = book.title,
        price = book.price,
        isbn = book.isbn
    )

    db.add(new_book)
    db.commit()
    db.refresh(new_book)        # DB에 반영된 정보(auo-increment인 id 포함)를 다시 읽어와서 new_book에 저장

    return new_book

# R
# 전체 조회
@router.get("/", response_model = list[Book])                # book들을 list 타입으로 엮어놓은거 생성 [{}, {}, ...]
async def getAll(db : Session = Depends(get_db)) -> dict:
    books = db.execute(select(BookModel).order_by(BookModel.id)).scalars().all()

    return books

# id 검색 조회
@router.get("/{id}", response_model= Book)
async def read_book(id : int = Path(...), db : Session = Depends(get_db)):
    book = db.get(BookModel, id)

    if book is None :
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "Id does not exist"
        )

    return book
    
# U
# id, 수정 내용 입력받아서 해당 Book 정보 수정
@router.put("/{id}", response_model= Book)
async def update_book(updated_book : BookInfo, id : int = Path(...), db : Session = Depends(get_db)):
    book = db.get(BookModel, id)

    if book is None :
        raise HTTPException(
            status_code= status.HTTP_404_NOT_FOUND,
            detail= "Id does not exist"
        )

    book.title = updated_book.title
    book.price = updated_book.price
    book.isbn = updated_book.isbn

    db.commit()
    db.refresh(book)
    return book

# D
# delete all 
@router.delete("/")
async def deleteAll(db: Session = Depends(get_db)) -> dict:
    result = db.execute(delete(BookModel))
    db.commit()

    if result.rowcount == 0:
        return { "message" : "삭제할 데이터가 없습니다." }
    return { "message" : "전체 데이터 삭제 완료" }

# 삭제할 책의 id 받아서 해당 책 삭제
@router.delete("/{id}")
async def delete_book(id : int = Path(...), db : Session = Depends(get_db)):
    delete_book = db.get(BookModel, id)

    if delete_book is None :
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="input id doesn't exist in DB",
        )

    db.delete(delete_book)
    db.commit()

    return { "message" : "삭제 완료" }