from pydantic import BaseModel, Field


class Hotel(BaseModel):
    title: str = Field(..., example="Hilton")
    location: str = Field(..., example="Moscow")

    class Config:
        from_attributes = True


class HotelPatch(BaseModel):
    title: str | None = Field(None)
    location: str | None = Field(None)

    class Config:
        from_attributes = True
