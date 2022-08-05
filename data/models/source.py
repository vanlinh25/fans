from pydantic import BaseModel
from typing import Union


class Source(BaseModel):
    src: Union[str, None] = None
    type: Union[str, None] = None


Source.update_forward_refs()
