from sqlalchemy.orm import DeclarativeBase, Mapped


class Base(DeclarativeBase):
    __abstract__ = True