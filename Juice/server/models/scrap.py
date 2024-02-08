from pydantic import BaseModel

class ScrapperModel(BaseModel):
    host: str
    params: list
    tag: str
    attrs: dict
    headers: dict
    data: dict
