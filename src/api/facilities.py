from fastapi import APIRouter

from src.api.dependencies import DBDep
from src.schemas.facility import FacilityAdd

router = APIRouter(prefix='/facilities', tags=['Facilities'])


@router.get('/')
async def get_facilities(db: DBDep,):
    return await db.facilities.get_all()


@router.post('')
async def create_facility(
        facility_data: FacilityAdd,
        db: DBDep,
):
    facility = await db.facilities.add(facility_data)
    await db.commit()
    return {'status': 'ok', 'data': facility}
