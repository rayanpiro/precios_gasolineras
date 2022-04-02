from backend.domain.repository_interface import IGasStationsRepository, IDistanceRepository
from backend.domain.models import LatType, LonType, DistanceType, GasStation, PetrolType, Gas95E10, Gas95E5, Gas95E5Premium, Gas98E10, Gas98E5, GasOilA, GasOilAPremium
from backend.application.gas_station_dto import GasStationDTO
from typing import Any, Type, Callable
from typing_extensions import Self

def str2PetrolType(x: str) -> Type[PetrolType] | None:
    petrol_types = {
    Gas95E5.__name__: Gas95E5,
    Gas95E5Premium.__name__: Gas95E5Premium,
    Gas95E10.__name__: Gas95E10,
    Gas98E5.__name__: Gas98E5,
    Gas98E10.__name__: Gas98E10,
    GasOilA.__name__: GasOilA,
    GasOilAPremium.__name__: GasOilAPremium,
    }
    return petrol_types.get(x)  # type: ignore

class GasStationService:
    def __init__(self, gas_stations_repo: IGasStationsRepository, distance_repo: IDistanceRepository):
        self._gas_stations_repo = gas_stations_repo
        self._distance_repo = distance_repo

    def refresh_data(self) -> Self:
        self._collect = self._gas_stations_repo.fetch_data()
        return self
    
    def get_stations(self) -> Self:
        self._collect = self._gas_stations_repo.get_cached()
        return self
    
    def sort_by_price(self, petrol_type_str: str | None) -> Self:
        
        if petrol_type_str == None:
            return self
        
        self.filter_by_petrol_type(petrol_type_str)

        petrol_type = str2PetrolType(petrol_type_str)

        if petrol_type == None:
            return self
        
        self._collect: list[GasStation] = sorted(
            self._collect,
            key = lambda x: x.price(petrol_type)
        )
        return self
    
    def filter_stations(self, sorting_condition: Callable[[GasStation], bool]) -> list[GasStation]:

        return list(
            filter(
                sorting_condition,
                self._collect
            )
        )

    def filter_by_ccaa(self, ccaa: str | None) -> Self:
        if ccaa != None:
            self._collect = self.filter_stations(lambda x: x.ccaa == ccaa)
        return self
    
    def filter_by_distance(self, search_radius: DistanceType | None, origin_lat: LatType | None, origin_lon: LonType | None) -> Self:
        if origin_lat != None and origin_lon != None and search_radius != None:
            origin_coords = (origin_lat, origin_lon)
            self._collect = self.filter_stations(lambda x: self._distance_repo.get_distance(origin_coords, x.coordinates) < search_radius)
        return self
    
    def filter_by_petrol_type(self, petrol_type_str: str) -> Self:
        petrol_type = str2PetrolType(petrol_type_str)
        if petrol_type == None:
            return self
        self._collect = self.filter_stations(lambda x: petrol_type in x.petrol_types)
        return self
    
    def collect(self, num_of_results:int | None) -> list[GasStationDTO]:
        return list(map(lambda x: GasStationDTO(x), self._collect))[0:num_of_results]

    def collect_json(self, num_of_results:int | None) -> list[dict[Any, Any]]:
        return list(map(lambda x: GasStationDTO(x).json, self._collect))[0:num_of_results]