from typing import List, Union
from beanie import Document

from data.models.video import Video
from data.models.image import Image

class Idol(Document):

    title: Union[str, None] = None
    url: str
    thumbnail: Union[str, None] = None
    full_image: Union[str, None] = None
    images: List[Image] = []
    videos: List[Video] = []

    class Settings:
        name = "fans"


Idol.update_forward_refs()
