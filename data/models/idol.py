from pydantic import BaseModel
from typing import Union

from .video import Video
from .image import Image

class Idol(BaseModel):
    title: Union[str, None] = None
    url: str
    thumbnail: Union[str, None] = None
    full_image: Union[str, None] = None
    images: list[Image]=[]
    videos: list=[Video]
    