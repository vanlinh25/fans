from pydantic import BaseModel
from typing import Union
import strawberry

class Source(BaseModel):
    src: Union[str, None] = None
    type: Union[str, None] = None

@strawberry.experimental.pydantic.type(model=Source, all_fields=True)
class SourceType:
    pass


Source.update_forward_refs()
