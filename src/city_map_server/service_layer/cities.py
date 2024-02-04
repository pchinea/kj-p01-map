from pydantic import UUID4

from city_map_server.service_layer.exceptions import CityAlreadyExistsException, CityDoesNotExistException
from sqlalchemy.exc import IntegrityError

from city_map_server.adapters.respositories.cities import CitiesAbstractRepository
from city_map_server.domain.cities import City


async def create_city(
        repo: CitiesAbstractRepository,
        name: str,
        country: str,
        latitude: float,
        longitude: float
) -> City:
    new_city = City(name=name, country=country, latitude=latitude, longitude=longitude)
    try:
        city = await repo.add_city(new_city)
    except IntegrityError:
        raise CityAlreadyExistsException(name=name)
    return city


async def get_city(repo: CitiesAbstractRepository, city_id: UUID4) -> City:
    city = await repo.get_city(city_id)
    if not city:
        raise CityDoesNotExistException(city_id=city_id)
    return city


async def list_cities(repo: CitiesAbstractRepository) -> list[tuple[UUID4, str]]:
    return await repo.get_city_names()
