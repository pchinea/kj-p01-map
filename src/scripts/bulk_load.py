import asyncio
import json
import os

from city_map_server.adapters.respositories.cities import CitiesSqlAlchemyRepository
from city_map_server.domain.cities import City
from city_map_server.service_layer import cities as cities_service

repo = CitiesSqlAlchemyRepository()


async def bulk_load():
    if await repo.is_empty():
        print("Load cities data...")
        script_directory = os.path.dirname(os.path.abspath(__file__))
        with open(os.path.join(script_directory, "cities.json")) as f:
            data = json.loads(f.read())

        print("Processing cities data...")
        cities = [City(**c) for c in data]

        print("Saving cities data...")
        await cities_service.bulk_insert_cities(repo, cities)

        print("Done.")

if __name__ == "__main__":
    asyncio.run(bulk_load())
