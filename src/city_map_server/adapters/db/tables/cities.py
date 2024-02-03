from sqlalchemy.orm import Mapped, mapped_column

from city_map_server.adapters.db.tables.base import Base


class City(Base):
    __tablename__ = "cities"

    country: Mapped[str]
    name: Mapped[str] = mapped_column(primary_key=True)
    lat: Mapped[str]
    lng: Mapped[str]
