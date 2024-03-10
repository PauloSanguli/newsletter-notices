"""running all services"""
from main import app

from src.schedule import CronJobs

import asyncio

import uvicorn


def run_api():
    """run fastapi with uvicorn"""
    uvicorn.run(
        app=app
    )

async def run_cron():
    """run the schedule service"""
    cron = CronJobs().get_cron()
    while True:
        cron.run_pending()
        await asyncio.sleep(1)

async def main():
    """create threads"""
    s_api = asyncio.to_thread(run_api)
    s_schedule = asyncio.create_task(run_cron())

    await asyncio.gather(s_api, s_schedule)

if __name__=="__main__":

    asyncio.run(main())