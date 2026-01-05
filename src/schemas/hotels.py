from pydantic import BaseModel, Field
from typing import Annotated


class Hotel(BaseModel):
    title: str = Field(..., example="Hilton")
    location: str = Field(..., example="Moscow")


    class Config:
        from_attributes = True