from beanie import PydanticObjectId
from fastapi import APIRouter
from typing import Union

from data.models.idol import Idol

router = APIRouter(prefix="/idols", tags=["Idols"])


@router.get("/", response_model=list[Idol])
async def read_item(size: Union[None, int] = 5):
    return await Idol.find_all().to_list(size)


@router.get("/{id}",response_model=Idol)
async def get_idol_by_id(id: PydanticObjectId):
    return await Idol.get(id)
