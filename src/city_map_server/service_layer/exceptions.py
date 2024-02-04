from uuid import UUID


class CityAlreadyExistsException(Exception):
    def __init__(self, name: str) -> None:
        self.name = name


class CityDoesNotExistException(Exception):
    def __init__(self, city_id: UUID) -> None:
        self.city_id = city_id
