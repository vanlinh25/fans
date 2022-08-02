from turtle import title
from pydantic import BaseModel
from typing import Union

class Video(BaseModel):
    source: list=[]
    fv_title: Union[str, None] = None
    splash: Union[str, None] = None

    