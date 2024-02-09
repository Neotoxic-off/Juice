import random
import requests
from bs4 import BeautifulSoup

from server.engine.invoker import Invoker
from server.models.scrap import ScrapperModel

class Core:
    def __init__(self):
        self.invoker = Invoker()

    def scrap(self, data: ScrapperModel):
        if (len(data.range) == 2):
            if (data.range[0] != data.range[1]):
                return (self.__multi_scrap__(data))

        return (self.__mono_scrap__(data))

    def __mono_scrap__(self, data: ScrapperModel):
        r = self.invoker.invoke(
            method=data.method,
            url=data.host,
            params=data.params,
            headers=data.headers,
            data=data.data,
            auth={}
        )

        return (self.__extract__(r.text, data.tag, data.element, data.attrs))

    def __multi_scrap__(self, data: ScrapperModel):
        buffer = []
        page = data.range[0]
        limit = data.range[1]

        for i in range(page, limit):
            self.__manage_params__(data.params, [data.ptag, i])

            r = self.invoker.invoke(
                method=data.method,
                url=data.host,
                params=data.params,
                headers=data.headers,
                data=data.data,
                auth={}
            )

            buffer += self.__extract__(r.text, data.tag, data.element, data.attrs)

        return (buffer)

    def __manage_params__(self, params: list, add: list):
        for i, element in enumerate(params):
            if (element[0] == element[0]):
                params[i][1] = add[1]

        return (params)

    def __extract__(self, html, tag, element, attrs):
        result = []

        soup = BeautifulSoup(html, 'html.parser')
        elements = soup.find_all(tag, attrs=attrs)

        for content in elements:
            if (element != None and len(element) > 0):
                result.append(content.get(element))
            else:
                result.append(content.text)

        return (result)