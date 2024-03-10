import schedule

from src.__bs.request import ScrapSystem

from src.notificate.sendEmail import Email

import asyncio

from typing import Type




class CronJobs:
    """automation with schedule"""
    def __init__(self):
        self.__cron = schedule
        self.set_jobs()

    def set_jobs(self):
        """set jobs"""
        scrapper = ScrapSystem()
        emailer = Email()

        self.__cron.every().day.at("10:00:00").do(scrapper.get_news())
        self.__cron.every().day.at("11:30:00").do(emailer.send())
    
    def get_cron(self):
        """return the schedule object"""
        return self.__cron
