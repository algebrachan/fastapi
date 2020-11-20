from fastapi import APIRouter
from common.entity import ResponseBase

base_router = APIRouter()

@base_router.get("/base")
async def base():

    res = ResponseBase()
    res.data = {"name":"wc"}

    return res