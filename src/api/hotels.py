from fastapi import APIRouter
from fastapi.params import Query

from src.api.dependencies import PaginationDep
from src.database import async_session_maker
from src.schemas.hotels import HotelPatch, HotelAdd
from src.repositories.hotels import HotelsRepository

router = APIRouter(prefix='/hotels', tags=['Hotels'])


@router.get('')
async def get_hotels(
    pagination: PaginationDep,
    location: str | None = Query(None),
    title: str | None = Query(None)
):

    per_page = pagination.per_page or 5
    async with async_session_maker() as session:
        return await HotelsRepository(session).get_all(
            location=location,
            title=title,
            limit=per_page,
            offset=per_page * (pagination.page - 1)
        )


@router.get('{/hotel_id}')
async def get_hotel(hotel_id: int):
    async with async_session_maker() as session:
        return await HotelsRepository(session).get_one_or_none(
            id=hotel_id,
        )


@router.post('')
async def create_hotel(hotel_data: HotelAdd):
    async with async_session_maker() as session:
        hotel = await HotelsRepository(session).add(hotel_data)
        await session.commit()

    return {'status': 'ok', 'data': hotel}


@router.put('/{hotel_id}')
async def update_hotel(hotel_data: HotelAdd, hotel_id: int):
    async with async_session_maker() as session:
        await HotelsRepository(session).update(hotel_data, id=hotel_id)
        await session.commit()

    return {'status': 'ok'}


@router.patch('/{hotel_id}')
async def partially_update_hotel(hotel_data: HotelPatch, hotel_id: int):
    async with async_session_maker() as session:
        await HotelsRepository(session).update(hotel_data, exclude_unset=True, id=hotel_id)
        await session.commit()

    return {'status': 'ok'}


@router.delete('/{hotel_id}')
async def delete_hotel(hotel_id: int):
    async with async_session_maker() as session:
        await HotelsRepository(session).delete(id=hotel_id)
        await session.commit()
    return {'status': 'ok'}
