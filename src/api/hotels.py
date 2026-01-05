from fastapi import APIRouter
from fastapi.params import Query
from sqlalchemy import insert, select, func

from src.api.dependencies import PaginationDep
from src.models.hotels import HotelsORM
from src.database import async_session_maker, engine
from src.schemas.hotels import Hotel

router = APIRouter(prefix='/hotels', tags=['Hotels'])


@router.get('', response_model=list[Hotel])
async def get_hotels(
    pagination: PaginationDep,
    location: str | None = Query(None),
    title: str | None = Query(None)
):

    per_page = pagination.per_page or 5

    async with async_session_maker() as session:
        query = select(HotelsORM)

        if location is not None:
            query = query.filter(func.lower(HotelsORM.location).contains(location.strip().lower()))

        if title is not None:
            query = query.filter(func.lower(HotelsORM.title).contains(title.strip().lower()))

        query = (
            query
            .limit(per_page)
            .offset(per_page * (pagination.page - 1))
        )

        print(query.compile(compile_kwargs={'literal_binds': True}))

        result = await session.execute(query)
        hotels = result.scalars().all()
        return hotels


@router.post('', response_model=Hotel)
async def create_hotel(hotel_data: Hotel):
    async with async_session_maker() as session:
        add_hotel_stmt = insert(HotelsORM).values(**hotel_data.model_dump())
        print(add_hotel_stmt.compile(engine, compile_kwargs={'literal_binds': True}))

        await session.execute(add_hotel_stmt)
        await session.commit()

    return hotel_data
