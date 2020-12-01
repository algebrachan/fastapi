from fastapi import APIRouter
from common.entity import ResponseBase
from services.base_service import q_course,add_course
from utils.log import logger
base_router = APIRouter()

@base_router.get("/base")
async def base():

    res = ResponseBase()
    res.data = q_course()
    logger.info('base')
    return res

@base_router.get("/add")
async def base():
    res = ResponseBase()
    add_course()
    return res
