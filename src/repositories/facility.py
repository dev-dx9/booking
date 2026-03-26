from src.models.facility import FacilityORM
from src.repositories.base import BaseRepository
from src.schemas.facility import Facility


class FacilityRepository(BaseRepository):
    model = FacilityORM
    schema = Facility
