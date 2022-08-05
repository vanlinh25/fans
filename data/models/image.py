from pydantic import BaseModel, Field
from typing import Union


class Image(BaseModel):
    title: Union[str, None] = None
    full_image: Union[str, None] = Field(default=None, alias='full')
    thumbnail: Union[str, None] = None
    thumbnail_3_2: Union[str, None] = Field(
        default=None, alias='3-2-thumbnail')


Image.update_forward_refs()
