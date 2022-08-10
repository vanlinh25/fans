from typing import List
import strawberry
from strawberry.fastapi import GraphQLRouter
from data.models.idol import Idol

@strawberry.experimental.pydantic.type(model=Idol)
class IdolType:
    title: strawberry.auto
    url: strawberry.auto
    thumbnail: strawberry.auto
    full_image: strawberry.auto
    # images: strawberry.auto
    # videos: strawberry.auto

    
@strawberry.type
class Query:
    @strawberry.field
    async def idols(self) -> List[IdolType]:
        return []


schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema,graphiql=True)
