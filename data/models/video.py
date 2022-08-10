from pydantic import BaseModel
from typing import List, Union
import strawberry

from data.models.source import Source


class Video(BaseModel):
    sources: List[Source] = []
    fv_title: Union[str, None] = None
    splash: Union[str, None] = None


@strawberry.experimental.pydantic.type(model=Video, all_fields=True)
class VideoType:
    pass


Video.update_forward_refs()
