base_url = "https://api.youneedabudget.com/v1"
from os import getenv
from . import models

import aiohttp

default_headers = {"Authorization": f"Bearer {getenv('YNAB_TOKEN')}"}

session = aiohttp.ClientSession(headers=default_headers)


async def scheduled_transactions(budget_id: str):
    async with session.get(f"{base_url}/budgets/{budget_id}/scheduled_transactions") as resp:
        return models.ScheduledTransactionsResponse(**await resp.json())
