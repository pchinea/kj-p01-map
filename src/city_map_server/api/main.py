from fastapi import FastAPI

from city_map_server.api.routers.cities import router

app = FastAPI()

app.include_router(router, prefix="/cities")
