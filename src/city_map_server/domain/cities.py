import uuid

from pydantic import BaseModel, ConfigDict, Field


class City(BaseModel):
    city_id: uuid.UUID = Field(default_factory=uuid.uuid4)
    country: str
    name: str
    latitude: float
    longitude: float

    model_config = ConfigDict(from_attributes=True)
