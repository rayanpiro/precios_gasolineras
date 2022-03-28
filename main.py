from backend.application.gas_station_service import GasStationService
from infraestructure.gob_gas_stations_repository import GasStationsRepository
from infraestructure.math_distance_repository import DistanceRepository
from backend.domain.models import Gas98E10, GasOilA

n=2

respuesta = GasStationService(
    GasStationsRepository(),
    DistanceRepository((37.403976,-5.9173506)),
    "Andalucia"
).get_stations().sort_by_price(GasOilA).sorted[0:10]

for station in respuesta:
    print(f'{station.name} - {station.location} - {station.opening_hours} - {station.maps_url} - {station.price(GasOilA)}')

