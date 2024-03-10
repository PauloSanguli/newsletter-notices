"""fetch datas from blog"""

import bs4
import requests

from src.infra.http.controllers import Controller

from .__links__ import LINKS



class ScrapSystem:
    def __init__(self):
        self.__links = LINKS
        self.get_content()
    
    def get_content(self):
        """get html"""
        self.__soups = list()
        for url in self.__links:
            html = requests.\
                get(f"{url}").content
            self.__soups.append(bs4.BeautifulSoup(html, 'html.parser'))

    
    def get_news(self, indx=0):
        """scrap datas from blog"""
        Controller.delete_all_newspapper()

        for soup in self.__soups:
            self.items = soup.find_all("div" ,class_="item-noticia")
            newspappers = list()

            for item in self.items:
                newspappers.append({
                    "header": item.select("h2")[0].get_text(),
                    "content": item.select("p")[0].get_text(),
                    "category": item.select("div.tag")[0].get_text(),
                    "img": "null",
                    "date_publish": item.select("div.data span:nth-of-type(1)")[0].get_text()
                })
            Controller.update_newspapper(newspappers)
