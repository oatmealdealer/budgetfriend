import asyncio
import logging
from datetime import tzinfo
from typing import List

import aiohttp
from fastapi import FastAPI

from app import ynab
import app.models as pg
from app.ynab.models import ScheduledTransactionDetail, ScheduledTransactionsResponse, ScheduledTransactionSummary

api = FastAPI()
session = aiohttp.ClientSession()


logging.basicConfig()
logging.getLogger().setLevel(logging.DEBUG)


@api.on_event("shutdown")
async def close_session():
    await session.close()
    await pg.database.disconnect()


@api.on_event("startup")
async def connect_db():
    await pg.database.connect()


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


@api.get("/users/", response_model=List[pg.User])
async def list_users():
    query = pg.users.select()
    return await pg.database.fetch_all(query)


@api.post("/users/", response_model=pg.User)
async def create_user(user: pg.UserInput):
    query = pg.users.insert().values(**user.dict(exclude_none=True)).returning(*pg.users.columns)
    result = await pg.database.fetch_one(query)
    return pg.User(**result)
