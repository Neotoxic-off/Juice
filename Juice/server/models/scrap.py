from pydantic import BaseModel

class ScraperModel(BaseModel):
    host: str
    params: list
    tag: str
    element: str
    attrs: dict
    headers: dict
    data: dict
    range: list
    method: str
    ptag: str
