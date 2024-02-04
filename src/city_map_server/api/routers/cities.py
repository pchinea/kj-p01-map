from fastapi import APIRouter, status, Query, HTTPException
from pydantic import UUID4

from city_map_server.adapters.respositories.cities import CitiesSqlAlchemyRepository
from city_map_server.api.schema.cities import City, CityBase
from city_map_server.service_layer import cities as cities_service
from city_map_server.service_layer.exceptions import CityDoesNotExistException

router = APIRouter()

repo = CitiesSqlAlchemyRepository()


@router.get("", response_model=list[CityBase])
async def get_all_cities(offset: int = 0, limit: int = Query(default=100, le=100)) -> list[CityBase]:
    return await cities_service.list_cities(repo, offset, limit)


@router.get("/{city_id}", response_model=City, status_code=status.HTTP_200_OK)
async def get_city(city_id: UUID4) -> City:
    try:
        return await cities_service.get_city(repo, city_id)
    except CityDoesNotExistException:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="City not found")

