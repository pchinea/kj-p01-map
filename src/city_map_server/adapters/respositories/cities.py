import abc
import uuid

from city_map_server.adapters.db.session import SessionManager
from city_map_server.domain.cities import City
from city_map_server.adapters.db.tables.cities import City as DB_City


class CitiesAbstractRepository(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    async def add_city(self, city: City):
        pass

    @abc.abstractmethod
    async def get_city(self, city_id: uuid.UUID):
        pass


class CitiesSqlAlchemyRepository(CitiesAbstractRepository):
    async def add_city(self, city: City) -> City | None:
        db_city = DB_City(**city.model_dump())
        async with SessionManager() as session:
            async with session.begin():
                session.add(db_city)
        return City.model_validate(db_city)

    async def get_city(self, city_id: uuid.UUID) -> City | None:
        async with SessionManager() as session:
            async with session.begin():
                db_city = await session.get(DB_City, city_id)
        if db_city:
            return City.model_validate(db_city)
