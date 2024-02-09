import os
from urllib.parse import urlencode

from server.engine.core import Core
from server.models.scrap import ScraperModel

from fastapi import FastAPI, Request, Depends, Response, APIRouter

router = APIRouter()
Scraper = Core()

@router.get("/")
async def get_home():
    return ({
        "data": "ok"
    })

@router.post("/scrap")
async def post_scrap(item: ScraperModel):
    return ({
        "result": Scraper.scrap(
            item
        )
    })
