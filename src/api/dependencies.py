from typing import Annotated

from fastapi import Depends, Query, Request, HTTPException, status
from pydantic import BaseModel

from src.services.auth import AuthService


class PaginationParams(BaseModel):
    page: Annotated[int, Query(default=1, ge=1)]
    per_page: Annotated[int | None, Query(None, ge=1, lt=30)]


PaginationDep = Annotated[PaginationParams, Depends()]


def get_token(request: Request) -> str:
    access_token = request.cookies.get('access_token', None)
    if not access_token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Access token not found',
        )
    return access_token


def get_current_user_id(token: str = Depends(get_token)) -> int | None:
    data = AuthService().decode_token(token)
    return data.get('user_id', None)


UserIdDep = Annotated[int, Depends(get_current_user_id)]
