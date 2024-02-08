import random
import requests
from bs4 import BeautifulSoup

from server.engine.invoker import Invoker
from server.models.scrap import ScrapperModel

class Core:
    def __init__(self):
        self.invoker = Invoker()

    def scrap(self, data: ScrapperModel):
        r = self.invoker.invoke(
            method="GET",
            url=data.host,
            params=data.params,
            headers=data.headers,
            data=data.data,
            auth={}
        )

        return self.__extract__(r.text, data.tag, data.attrs)

    def __extract__(self, html, tag, attrs):
        result = []

        soup = BeautifulSoup(html, 'html.parser')

        elements = soup.find_all(tag, attrs=attrs)
        for element in elements:
            result.append(f"{element}")

        return (result)