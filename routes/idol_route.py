from beanie import PydanticObjectId
from fastapi import APIRouter
from typing import Union

from data.models.idol import Idol

router = APIRouter(prefix="/idols", tags=["Idols"])


@router.get("/", response_model=list[Idol])
async def get_all_idols(size: Union[None, int] = 5, page: Union[None, int] = 1) -> list[Idol]:
    return await Idol.find_all().skip((page-1)*size).limit(size).to_list()


@router.get("/{id}", response_model=Idol)
async def find_idol_by_id(id: PydanticObjectId) -> Idol:
    return await Idol.get(id)
