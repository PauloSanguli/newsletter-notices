"""fetch datas from blog"""

import bs4
import requests

from src.infra.http.controllers import Controller

from .__links__ import LINKS

from requests.exceptions import ConnectionError


class ScrapSystem:
    def __init__(self):
        self.__links = LINKS
        self.get_content()
    
    def get_content(self):
        """get html"""
        try:
            self.__soups = list()
            for url in self.__links:
                html = requests.\
                    get(f"{url}").content
                self.__soups.append(bs4.BeautifulSoup(html, 'html.parser'))
        except ConnectionError:
            print("dont connected")
            self.error_connecting = True

    
    def get_news(self):
        """scrap datas from blog"""
        Controller.delete_all_newspapper()
        try:
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
        except:
            print("check your conection and try later")
            return "check your conection and try later", False
        if self.error_connecting:
            return "check your conection and try later", False
        return "", True