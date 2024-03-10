import schedule

from src.__bs.request import ScrapSystem

from src.notificate.sendEmail import Email

import asyncio




class CronJobs:
    """automation with schedule"""
    def __init__(self):
        self.__cron = schedule

    def set_jobs(self):
        """set jobs"""
        scrapper = ScrapSystem()
        emailer = Email()

        self.__cron.every().day.at("10:00:00").do(scrapper.get_news())
        self.__cron.every().day.at("11:30:00").do(emailer.send())
    
    async def run_cron(self):
        """run the schedule service"""
        while True:
            self.__cron.run_pending()
            await asyncio.sleep(1)
