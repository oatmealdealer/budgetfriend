from app.fast_api import api

# from app.graphql import router
import asyncio
from datetime import datetime
from typing import Optional
import app.models as pg

import strawberry
from strawberry.fastapi import GraphQLRouter


@strawberry.type
class User:
    id: int
    first_name: str
    last_name: str
    created_at: Optional[datetime]


@strawberry.type
class Query:
    @strawberry.field
    async def user(self) -> User:
        query = pg.users.select()
        result = await pg.database.fetch_one(query)
        return User(**result)


schema = strawberry.Schema(Query)
router = GraphQLRouter(schema)


api.include_router(router, prefix="/graphql")
