import json
import requests
import urllib.parse

class Nyaa:
    def __init__(self):
        self.host = "https://nyaa.si"
        self.pages = 101
        self.links = []

        self.__get__()

    def get_name_from_magnet(self, magnet_link):
        if magnet_link.startswith("magnet:?xt=urn:btih:"):
            params = magnet_link.split('&')
            for param in params:
                if param.startswith('dn='):
                    name_encoded = param[3:]
                    name_decoded = urllib.parse.unquote(name_encoded)
                    return name_decoded
        
        return None

    def __get__(self):
        r = requests.post("http://127.0.0.1:8081/scrap", json = {
            "method": "GET",
            "host": self.host,
            "params": [],
            "tag": "a",
            "element": "href",
            "attrs": {},
            "headers": {},
            "data": {},
            "range": [0, self.pages],
            "ptag": "p"
        })

        for result in r.json()["result"]:
            if (result.startswith("magnet:") == True and result not in self.links):
                name = self.get_name_from_magnet(result).encode().decode('unicode_escape')
                self.links.append({
                    "name": name,
                    "magnet": result
                })
        self.__dump__()

    def __dump__(self):
        with open("links.json", "w+") as f:
            f.write(json.dumps(self.links, indent=4))

if (__name__ == "__main__"):
    Nyaa()
