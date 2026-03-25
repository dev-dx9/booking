from src.models.booking import BookingORM
from src.repositories.base import BaseRepository
from src.schemas.bookings import Booking


class BookingsRepository(BaseRepository):
    model = BookingORM
    schema = Booking
