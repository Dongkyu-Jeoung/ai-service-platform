from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column
from database import Base

class TodoModel(Base):
    __tablename__ = "todos"

    id: Mapped[int] = mapped_column(            # integer type
        primary_key=True,
        autoincrement=True
    )           
    item: Mapped[str] = mapped_column(          # varchar type
        String(200),                            # varchar(200)
        nullable=False                          # NOT NULL
    )         