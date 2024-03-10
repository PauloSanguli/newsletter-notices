"""running all services"""
from .main import app

from src.schedule import CronJobs

import asyncio

import uvicorn


async def run_api():
    """run fastapi with uvicorn"""
    uvicorn.run(
        app=app
    )

async def main():
    """create threads"""
    s_api = asyncio.to_thread(run_api)
    s_schedule = asyncio.create_task(CronJobs.run_cron())

    asyncio.gather(s_api, s_schedule)

if __name__=="__main__":
    asyncio.run(main)