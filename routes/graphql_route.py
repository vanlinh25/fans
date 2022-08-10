from typing import List, Optional
import strawberry
from strawberry.fastapi import GraphQLRouter
from bson.objectid import ObjectId

from configs.db import getDB
from data.models.idol import Idol, IdolType

@strawberry.type
class Query:
    @strawberry.field
    async def idols(self,size: Optional[int] = 5,page: Optional[int] = 1) -> List[IdolType]:
        fans = getDB()["fans"].find().skip((page-1)*size).limit(size)
        return [IdolType.from_pydantic(Idol(**fan)) for fan in fans]

    @strawberry.field
    async def idol(self, id: str) -> IdolType:
        fan = getDB()["fans"].find_one({"_id":ObjectId(id)})
        return IdolType.from_pydantic(Idol(**fan))

schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema, graphiql=True)
