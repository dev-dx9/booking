from pydantic import BaseModel, Field


class FacilityAdd(BaseModel):
    title: str = Field(..., example="wi-fi")


class Facility(FacilityAdd):
    id: int
