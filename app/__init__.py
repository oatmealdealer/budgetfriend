import asyncio
import logging
from datetime import tzinfo

import aiohttp
from fastapi import FastAPI

from app import ynab
from app.models import *
from app.ynab.models import ScheduledTransactionDetail, ScheduledTransactionsResponse, ScheduledTransactionSummary

api = FastAPI()
session = aiohttp.ClientSession()


logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


@api.on_event("shutdown")
async def close_session():
    await session.close()
    await database.disconnect()


@api.on_event("startup")
async def connect_db():
    await database.connect()


async def fetch(url: str, *, headers=None):
    async with session.get(url, headers=headers) as resp:
        return await resp.json()


@api.get("/budgets")
async def get_budgets():
    resp = await fetch(ynab.base_url + "/budgets", headers=ynab.default_headers)
    return resp


@api.get("/budgets/{budget_id}/scheduled_transactions")
async def get_scheduled_transactions(budget_id: str) -> List[ScheduledTransactionDetail]:
    resp = await ynab.scheduled_transactions(budget_id)
    return resp.data.scheduled_transactions


@api.get("/users/", response_model=List[User])
async def list_users():
    query = users.select()
    return await database.fetch_all(query)


@api.post("/users/", response_model=User)
async def create_user(user: UserInput):
    query = users.insert().values(**user.dict(exclude_none=True)).returning(*users.columns)
    result = await database.fetch_one(query)
    return User(**result)
