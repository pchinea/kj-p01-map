from pydantic import BaseModel, ConfigDict


class City(BaseModel):
    country: str
    name: str
    lat: str
    lng: str

    model_config = ConfigDict(from_attributes=True)
