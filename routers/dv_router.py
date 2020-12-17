from fastapi import APIRouter
from common.entity import ResponseBase
from utils.log import logger
from services.dv_service import * 

dv_router = APIRouter()


@dv_router.get("/get_total_count", summary='获取总体数据', description='包括 放肩、等径的在线误检等数据')
async def get_total_count():
    res = ResponseBase()
    # 传值
    total_count(res)
    return res
