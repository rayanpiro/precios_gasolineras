from backend.domain.models import GasStation, PetrolPriceType

class GasStationDTO():
    def __init__(self, object: GasStation):
        self.name = object.name
        self.location = object.location
        # self.coordinates = object.coordinates
        self.maps_url = object.maps_url
        self.opening_hours = object.opening_hours
        self.petrols: dict[str, PetrolPriceType] = dict( [ (key.__name__, object.price(key)) for key in object.petrol_types ] )   # type: ignore
        self.ccaa = object.ccaa
    
    @property
    def __name__(self):
        return "result"
    
    def __iter__(self):
        yield (self.__name__, self.__dict__)
    
    @property
    def json(self):
        return dict(self)