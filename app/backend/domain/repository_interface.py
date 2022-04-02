import abc
from .models import GasStation, CoordinatesType, DistanceType

class IGasStationsRepository(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def fetch_data(self) -> list[GasStation]:
        raise NotImplementedError
    
    @abc.abstractmethod
    def get_cached(self) -> list[GasStation]:
        raise NotImplementedError

class IDistanceRepository(metaclass=abc.ABCMeta):
    
    @abc.abstractmethod
    def get_distance(self, user_coords: CoordinatesType, destination_coords: CoordinatesType) -> DistanceType:
        raise NotImplementedError