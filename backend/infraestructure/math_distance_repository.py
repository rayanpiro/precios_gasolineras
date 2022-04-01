from backend.domain.repository_interface import IDistanceRepository
from backend.domain.models import CoordinatesType, DistanceType
from math import pi, sin, cos, atan2, sqrt, pow

def deg2rad(x: CoordinatesType) -> CoordinatesType:
    return (
        x[0] * pi / 180,
        x[1] * pi / 180
    )

def get_distance_in_meters(origin_rads: CoordinatesType, destination_rads: CoordinatesType, radius: float) -> DistanceType:
    a = pow(
        sin( (destination_rads[0] - origin_rads[0]) / 2 ),
        2) + cos(destination_rads[0]) * cos(origin_rads[0]) * pow(
            sin( (destination_rads[1] - origin_rads[1]) / 2 ),
            2
        )
    c = 2 * atan2(sqrt(a), sqrt(1-a))

    return radius * c

class DistanceRepository(IDistanceRepository):
    def __init__(self):
        self._radius = 6371e3
    
    def get_distance(self, user_coords: CoordinatesType, destination_coords: CoordinatesType) -> DistanceType:
        user_coords_rad = deg2rad(user_coords)
        dest_coords_rad = deg2rad(destination_coords)

        return get_distance_in_meters(user_coords_rad, dest_coords_rad, self._radius)