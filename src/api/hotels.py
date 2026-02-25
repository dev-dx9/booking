from fastapi import APIRouter
from fastapi.params import Query

from src.api.dependencies import PaginationDep, DBDep
from src.schemas.hotels import HotelPatch, HotelAdd

router = APIRouter(prefix='/hotels', tags=['Hotels'])


@router.get('')
async def get_hotels(
        db: DBDep,
        pagination: PaginationDep,
        location: str | None = Query(None),
        title: str | None = Query(None),
):
    per_page = pagination.per_page or 5
    return await db.hotels.get_all(
        location=location,
        title=title,
        limit=per_page,
        offset=per_page * (pagination.page - 1)
    )


@router.get('/{hotel_id}')
async def get_hotel(
        db: DBDep,
        hotel_id: int,
):
    return await db.hotels.get_one_or_none(
        id=hotel_id,
    )


@router.post('')
async def create_hotel(
        db: DBDep,
        hotel_data: HotelAdd,
):
    hotel = await db.hotels.add(hotel_data)
    await db.commit()
    return {'status': 'ok', 'data': hotel}


@router.put('/{hotel_id}')
async def update_hotel(
        db: DBDep,
        hotel_data: HotelAdd,
        hotel_id: int,
):
    await db.hotels.update(hotel_data, id=hotel_id)
    await db.commit()
    return {'status': 'ok'}


@router.patch('/{hotel_id}')
async def partially_update_hotel(
        db: DBDep,
        hotel_data: HotelPatch,
        hotel_id: int,
):
    await db.hotels.update(hotel_data, exclude_unset=True, id=hotel_id)
    await db.commit()
    return {'status': 'ok'}


@router.delete('/{hotel_id}')
async def delete_hotel(
        db: DBDep,
        hotel_id: int
):
    await db.hotels.delete(id=hotel_id)
    await db.commit()
    return {'status': 'ok'}
