from city_map_server.service_layer.exceptions import CityAlreadyExistsException, CityDoesNotExistException
from sqlalchemy.exc import IntegrityError

from city_map_server.adapters.respositories.cities import CitiesAbstractRepository
from city_map_server.domain.cities import City


async def create_city(
        repo: CitiesAbstractRepository,
        name: str,
        country: str,
        lat: str,
        lng: str
) -> City:
    new_city = City(name=name, country=country, lat=lat, lng=lng)
    try:
        city = await repo.add_city(new_city)
    except IntegrityError:
        raise CityAlreadyExistsException(name=name)
    return city
