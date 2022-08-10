from pydantic import BaseModel
from typing import List, Union

from data.models.source import Source


class Video(BaseModel):
    sources: List[Source] = []
    fv_title: Union[str, None] = None
    splash: Union[str, None] = None


Video.update_forward_refs()
