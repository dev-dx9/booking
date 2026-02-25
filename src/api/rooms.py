from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.rooms import RoomAdd, RoomAddRequest, RoomPatchRequest, RoomPatch

router = APIRouter(prefix='/hotels', tags=['Rooms'])


@router.get('/{hotel_id}/rooms')
async def get_rooms(
        hotel_id: int,
        db: DBDep,
):
    return await db.rooms.get_filtered(hotel_id=hotel_id)


@router.get('/{hotel_id}/rooms{room_id}')
async def get_room(
        hotel_id: int,
        room_id: int,
        db: DBDep,
):
    return await db.rooms.get_one_or_none(
        hotel_id=hotel_id,
        id=room_id,
    )


@router.post('/{hotel_id}/rooms')
async def create_room(
        hotel_id: int,
        room_data: RoomAddRequest,
        db: DBDep,
):
    _room_data = RoomAdd(hotel_id=hotel_id, **room_data.model_dump())
    room = await db.rooms.add(_room_data)
    await db.commit()
    return {'status': 'ok', 'data': room}


@router.put('/{hotel_id}/rooms/{room_id}')
async def update_room(
        hotel_id: int,
        room_id: int,
        room_data: RoomAddRequest,
        db: DBDep,
):
    _room_data = RoomAdd(hotel_id=hotel_id, **room_data.model_dump())
    await db.rooms.update(_room_data, id=room_id)
    await db.commit()
    return {'status': 'ok'}


@router.patch('/{hotel_id}/rooms/{room_id}')
async def partially_update_hotel(
        hotel_id: int,
        room_id: int,
        room_data: RoomPatchRequest,
        db: DBDep,
):
    _room_data = RoomPatch(hotel_id=hotel_id, **room_data.model_dump(exclude_unset=True))
    await db.rooms.update(
        _room_data,
        exclude_unset=True,
        hotel_id=hotel_id,
        id=room_id,
    )
    await db.commit()
    return {'status': 'ok'}


@router.delete('/{hotel_id}/rooms/{room_id}')
async def delete_room(
        hotel_id: int,
        room_id: int,
        db: DBDep,
):
    await db.rooms.delete(
        hotel_id=hotel_id,
        id=room_id,
    )
    await db.commit()
    return {'status': 'ok'}
