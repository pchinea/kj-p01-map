import asyncio
import json

from city_map_server.adapters.respositories.cities import CitiesSqlAlchemyRepository
from city_map_server.domain.cities import City
from city_map_server.service_layer import cities as cities_service

repo = CitiesSqlAlchemyRepository()


async def bulk_load():
    if await repo.is_empty():
        print("Load cities data...")
        with open("cities.json") as f:
            data = json.loads(f.read())

        print("Processing cities data...")
        cities = [City(**c) for c in data]

        print("Saving cities data...")
        await cities_service.bulk_insert_cities(repo, cities)

        print("Done.")

if __name__ == "__main__":
    asyncio.run(bulk_load())
