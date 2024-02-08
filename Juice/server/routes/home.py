import os
from urllib.parse import urlencode

from server.engine.core import Core
from server.models.scrap import ScrapperModel

from fastapi import FastAPI, Request, Depends, Response, APIRouter

router = APIRouter()
scrapper = Core()

@router.get("/")
async def get_home():
    return ({
        "data": "ok"
    })

@router.post("/scrap/")
async def post_scrap(item: ScrapperModel):
    return ({
        "result": scrapper.scrap(
            item
        )
    })
