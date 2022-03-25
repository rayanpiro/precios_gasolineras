PetrolPriceType = float

class PetrolType:

    def __init__(self, price: PetrolPriceType):
        self._price = price
    
    @property
    def price(self) -> PetrolPriceType:
        return self._price

class Gas95Octanes(PetrolType):
    pass

class Gas98Octanes(PetrolType):
    pass

class GasOil(PetrolType):
    pass

CoordinatesType = tuple[float, float]
class GasStation:
    def __init__(self, name: str, location: str, coordinates: CoordinatesType, opening_hours: str, petrols: dict[PetrolType, PetrolType]):
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

    def price(self, petrol: PetrolType) -> PetrolPriceType:
        
        get_petrol_instance = self._petrols.get(petrol)
        
        if get_petrol_instance == None:
            raise NoPetrolTypeFoundError(f'The petrol type {petrol} is not present.', self._petrols)
        return get_petrol_instance.price

    def get_googlemaps_url(self) -> str:
        if len(self._coordinates) == 2:
            return f'https://www.google.com/maps/search/?api=1&query={self._coordinates[0]},{self._coordinates[1]}'
        raise BadCoordinatesError('Bad coordinates.', self._coordinates)

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

