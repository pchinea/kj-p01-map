import uuid

from sqlalchemy.orm import Mapped, mapped_column

from city_map_server.adapters.db.tables.base import Base


class City(Base):
    __tablename__ = "cities"

    city_id: Mapped[uuid.UUID] = mapped_column(primary_key=True)
    country: Mapped[str]
    name: Mapped[str]
    latitude: Mapped[float]
    longitude: Mapped[float]
