from fastapi import APIRouter
from common.entity import ResponseBase
from utils.log import logger
from services.dv_service import *

dv_router = APIRouter()


@dv_router.get('/get_total_count', summary='获取总体数据', description='包括 放肩、等径的在线误检等数据 当天')
async def get_total_count():
    res = ResponseBase()
    # 传值
    total_count(res)
    return res


@dv_router.get('/get_series_count', summary='获取系列断苞信息', description='放肩断苞，等径断苞')
async def get_series_count():
    res = ResponseBase()
    series_count(res)
    return res


@dv_router.get('/get_total_shoulder_data', summary='获取放肩总计数据', description='包括 当日扩肩成活比例，扩断长度分布，扩断历史数据')
async def get_total_shoulder_data():
    res = ResponseBase()
    total_shoulder_data(res)
    return res


@dv_router.get('/get_total_diameter_data', summary='获取等径总计数据', description='包括 当日等径成活比例，断苞长度分布，等径断苞历史数据跟踪')
async def get_total_diameter_data():
    res = ResponseBase()
    total_diameter_data(res)
    return res


@dv_router.get('/get_total_rates', summary='获取总体数率', description='各工艺过程受控占比')
async def get_total_rates():
    res = ResponseBase()
    total_rates(res)
    return res


@dv_router.get('/get_total_normal_disb', summary='获取正态分布数据', description='稳温工时,引晶拉速,放肩长度,等径偏差')
async def get_total_normal_disb():
    res = ResponseBase()
    total_normal_disb(res)
    return res