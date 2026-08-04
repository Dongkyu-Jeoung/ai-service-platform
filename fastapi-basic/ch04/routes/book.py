# =========================================================
# 도서 관리 어플리케이션
# =========================================================


from fastapi import APIRouter, Path, HTTPException, status
from ch03.schemas.book_schema import Book

router = APIRouter()

book_list = []

# C
@router.post("/")
async def add_book(new_book : Book) -> dict:
    book_list.append(new_book)
    return {
        "message" : "등록 완료 되었습니다."
    }

# R
# 전체 조회
@router.get("/")
async def getAll() -> dict:
    return {
        "bookList" : book_list
    }

# id 검색 조회
@router.get("/{id}")
async def read_book(id : int = Path(...)):
    for book in book_list:
        if id == book.id:
            return {
                "result" : book
            }
        
    return { "message" : "책의 id를 확인해주세요" } 

# U
# id, 수정 내용 입력받아서 해당 Book 정보 수정
@router.put("/{id}")
async def update_book(updated_book : Book, id : int = Path(...)):
    for idx, book in enumerate(book_list):
        if id == book.id:
            book_list[idx] = updated_book
            return {
                "result" : "수정이 완료 되었습니다."
            }

    return { "message" : "책의 id를 확인해주세요" } 

# D
# delete all 
@router.delete("/")
async def deleteAll() -> dict:
    if len(book_list) > 0 :
        book_list.clear()
        return {
            "message" : "전체 목록 삭제 완료"
        }
    return { "message" : "삭제할 목록이 없습니다." }

# 삭제할 책의 id 받아서 해당 책 삭제
@router.delete("/{id}")
async def delete_book(id : int = Path(...)):
    for idx in range(len(book_list)):
        if book_list[idx].id == id:
            book_list.pop(idx)
            return { "message" : "삭제 완료" }
    return { "message" : "id를 확인해주세요" }