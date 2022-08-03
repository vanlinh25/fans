from pydantic import Field
from typing import Union
from beanie import Document

from data.models.video import Video
from data.models.image import Image

class Idol(Document):

    title: Union[str, None] = None
    url: str
    thumbnail: Union[str, None] = None
    full_image: Union[str, None] = Field(default=None, alias='full')
    images: list[Image] = []
    videos: list[Video] = []
    
    class Settings:
        name = "fans"

Idol.update_forward_refs()