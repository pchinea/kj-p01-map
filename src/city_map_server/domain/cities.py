from pydantic import BaseModel, ConfigDict


class City(BaseModel):
    country: str
    name: str
    latitude: float
    longitude: float

    model_config = ConfigDict(from_attributes=True)
