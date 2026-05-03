from src.models.facility import FacilityORM, RoomFacilityORM
from src.repositories.base import BaseRepository
from src.schemas.facility import Facility, RoomFacility


class FacilityRepository(BaseRepository):
    model = FacilityORM
    schema = Facility


class RoomFacilityRepository(BaseRepository):
    model = RoomFacilityORM
    schema = RoomFacility
