from pydantic import BaseModel
from typing import Union


class Image(BaseModel):
    title: Union[str, None] = None
    full_image: Union[str, None] = None
    thumbnail: Union[str, None] = None
    thumbnail_3_2: Union[str, None] = None


Image.update_forward_refs()
