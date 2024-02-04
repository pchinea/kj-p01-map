from pydantic import BaseModel, ConfigDict


class City(BaseModel):
    country: str
    name: str
    latitude: str
    longitude: str

    model_config = ConfigDict(from_attributes=True)
