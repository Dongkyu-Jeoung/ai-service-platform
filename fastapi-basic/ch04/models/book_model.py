from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class BookModel(Base):
    __tablename__ = "books"

    id: Mapped[int] = mapped_column(            # integer type
        primary_key=True,
        autoincrement=True
    )           
    title: Mapped[str] = mapped_column(          # varchar type
        String(200),                            # varchar(200)
        nullable=False                          # NOT NULL
    )

    price: Mapped[int] = mapped_column(
        Integer,
        nullable=True
    )
    isbn: Mapped[int] = mapped_column(
        Integer,
        nullable= False
    )             