"""fetch datas from blog"""

import bs4
import requests

from src.infra.http.controllers import Controller


class ScrapSystem:
    def __init__(self):
        self.get_content()
    
    def get_content(self):
        """get html"""
        html = requests.\
            get("https://www.jornaldeangola.ao/ao/noticias/index.php?tipo=1&idSec=16").content
        self.soup = bs4.BeautifulSoup(html, 'html.parser')

    
    def get_news(self):
        """scrap datas from blog"""
        self.items = self.soup.find_all("div" ,class_="item-noticia")
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
