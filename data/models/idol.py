from typing import List, Union
from beanie import Document
import strawberry

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

@strawberry.experimental.pydantic.type(model=Idol)
class IdolType:
    id:str
    title: strawberry.auto
    url: strawberry.auto
    thumbnail: strawberry.auto
    full_image: strawberry.auto
    images: strawberry.auto
    videos: strawberry.auto


Idol.update_forward_refs()
