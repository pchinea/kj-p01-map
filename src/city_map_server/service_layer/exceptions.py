
class CityAlreadyExistsException(Exception):
    def __init__(self, name: str) -> None:
        self.name = name


class CityDoesNotExistException(Exception):
    def __init__(self, name: str) -> None:
        self.name = name