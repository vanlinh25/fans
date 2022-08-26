from pydantic import BaseModel
from typing import Union
import strawberry


class Image(BaseModel):
    title: Union[str, None] = None
    full_image: Union[str, None] = None
    thumbnail: Union[str, None] = None
    thumbnail_3_2: Union[str, None] = None


@strawberry.experimental.pydantic.type(model=Image, all_fields=True)
class ImageType:
    pass


Image.update_forward_refs()
