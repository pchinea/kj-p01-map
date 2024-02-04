import uuid

from pydantic import BaseModel, ConfigDict, Field


class CityBase(BaseModel):
    city_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    name: str


class City(CityBase):
    country: str
    latitude: float
    longitude: float

    model_config = ConfigDict(from_attributes=True)
