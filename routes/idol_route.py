from fastapi import APIRouter
from typing import Union
from bson import json_util
import json

from data.models.idol import Idol
from configs.db import fan

router = APIRouter(prefix="/idols", tags=["Idols"])

def parse_json(data):
    return json.loads(json_util.dumps(data))

@router.get("/")
def read_item(size:Union[None,int]=5):
    fans = list(fan.find().limit(size))
    return parse_json(fans)


@router.get("/{idol_id}")
def get_idol_by_id(idol_id: str):
    return {"hello":idol_id}
