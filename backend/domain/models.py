from typing_extensions import Self
from typing import Type

DistanceType = float
DurationType = str

PetrolPriceType = float

class PetrolType:

    def __init__(self, price: PetrolPriceType):
        self._price = price
    
    def __le__(self, other: Self) -> bool:
        return self.price < other.price
    
    @property
    def price(self) -> PetrolPriceType:
        return self._price

    @property
    def __name__(self) -> str:
        return "PetrolType"

class Gas95E5(PetrolType):
    @property
    def __name__(self) -> str:
        return "Gas95E5"

class Gas95E5Premium(PetrolType):
    @property
    def __name__(self) -> str:
        return "Gas95E5Premium"

class Gas95E10(PetrolType):
    @property
    def __name__(self) -> str:
        return "Gas95E10"

class Gas98E5(PetrolType):
    @property
    def __name__(self) -> str:
        return "Gas98E5"

class Gas98E10(PetrolType):
    @property
    def __name__(self) -> str:
        return "Gas98E10"

class GasOilA(PetrolType):
    @property
    def __name__(self) -> str:
        return "GasOilA"

class GasOilAPremium(PetrolType):
    @property
    def __name__(self) -> str:
        return "GasOilAPremium"

LatType = float
LonType = float
CoordinatesType = tuple[LatType, LonType]

class GasStation:
    def __init__(self, name: str, location: str, coordinates: CoordinatesType, opening_hours: str, petrols: dict[Type[PetrolType], PetrolType]):
        self._name = name
        self._location = location
        self._coordinates = coordinates
        self._maps_url = self.get_googlemaps_url()
        self._opening_hours = opening_hours
        self._petrols = petrols

    @property
    def name(self) -> str:
        return self._name

    @property
    def location(self) -> str:
        return self._location

    @property
    def maps_url(self) -> str:
        return self._maps_url

    @property
    def coordinates(self) -> CoordinatesType:
        return self._coordinates

    @property
    def opening_hours(self) -> str:
        return self._opening_hours

    @property
    def petrol_types(self) -> list[Type[PetrolType]]:
        return list(self._petrols.keys())

    def price(self, petrol: Type[PetrolType]) -> PetrolPriceType:
        
        get_petrol_instance = self._petrols.get(petrol)
        
        if get_petrol_instance == None:
            raise NoPetrolTypeFoundError(f'The petrol type {petrol} is not present.', self._petrols)
        return get_petrol_instance.price
    
    def get_googlemaps_url(self) -> str:
        if len(self._coordinates) != 2:
            raise BadCoordinatesError('Bad coordinates.', self._coordinates)
        return f'https://www.google.com/maps/search/?api=1&query={self._coordinates[0]},{self._coordinates[1]}'
    
    def __le__(self, other: Self, petrol_criteria: Type[PetrolType]) -> bool:
        if petrol_criteria not in self.petrol_types or petrol_criteria not in other.petrol_types:
            raise NotImplementedError
        return self.price(petrol_criteria) < other.price(petrol_criteria)

class GasStationExceptions(Exception):
    """ Base class for other exceptions """
    pass

class UnkwnownError(GasStationExceptions):
    """ Raised when an unknown error has ocurred """
    pass

class CreationError(GasStationExceptions):
    """ Raised when there is a problem initializating GasStation """
    pass

class BadCoordinatesError(GasStationExceptions):
    """ Raised when there is a problem with coordinates """
    pass

class NoPetrolTypeFoundError(GasStationExceptions):
    """ Raised when there is no the specified PetrolType on this GasStation """
    pass

