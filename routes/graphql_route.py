import typing
import strawberry
from strawberry.fastapi import GraphQLRouter
from data.models.idol import Idol

@strawberry.type
class IdolDto:
    id:str
    url: str
    title: str
    thumbnail: str
    full_image: str

def idol_mapper(idol:Idol)->IdolDto:
    return IdolDto(idol.id,idol.url,idol.title,idol.thumbnail,idol.full_image)

async def get_idols():
    idols=[]
    return [
        idol_mapper(idol) for idol in idols
    ]


@strawberry.type
class Query:
    idols: typing.List[IdolDto] = strawberry.field(resolver=get_idols)


schema = strawberry.Schema(Query)

graphql_app = GraphQLRouter(schema)
