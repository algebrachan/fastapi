from common.entity import ResponseBase, Error
from common.response import *
from utils.log import logger
import random


def total_count(res: ResponseBase):
    try:
        data = RespGetTotalCount()
        data.diameter = CommonCount(1, 2, 3, 4)
        data.shoulder = CommonCount(5, 6, 7, 10)
        res.data = data
    except Exception as e:
        res.error(Error.SERVER_EXCEPTION)
        logger.error(e)
    return res


def series_count(res: ResponseBase):
    try:
        data = RespGetSeriesCount()
        for s in [chr(i) for i in range(65, 71)]:
            item_s = CommonListItem(s, ord(s))
            item_d = CommonListItem(s, 200-ord(s))
            data.shoulder.append(item_s)
            data.diameter.append(item_d)
        res.data = data
    except Exception as e:
        res.error(Error.SERVER_EXCEPTION)
        logger.error(e)
    return res


def total_shoulder_data(res: ResponseBase):
    try:
        data = RespTotalShoulderData()
        data.succ = 230
        data.total = 300
        data.rate = round(data.succ/data.total, 4)
        for i in ['1', '3', '5', '7', '9', '11']:
            item = CommonListItem(i, random.randint(1, 100))
            data.distribution.append(item)
        for i in ['12-01', '12-03', '12-05', '12-07', '12-09', '12-11', '12-13']:
            item = CommonListItem(i, random.randint(100, 200))
            data.history.append(item)

        res.data = data
    except Exception as e:
        res.error(Error.SERVER_EXCEPTION)
        logger.error(e)

    return res


def total_diameter_data(res: ResponseBase):
    try:
        data = RespTotalDiameterData()
        data.succ = 200
        data.total = 300
        data.rate = round(data.succ/data.total, 4)
        for i in ['1', '3', '5', '7', '9', '11']:
            item = CommonListItem(i, random.randint(1, 100))
            data.distribution.append(item)
        for i in ['12-01', '12-03', '12-05', '12-07', '12-09', '12-11', '12-13']:
            item = CommonListItem(i, random.randint(100, 200))
            data.history.append(item)
        res.data = data
    except Exception as e:
        res.error(Error.SERVER_EXCEPTION)
        logger.error(e)
    return res


def total_rates(res: ResponseBase):
    try:
        data = RespTotalRates()
        data.accuracy = 0.98
        data.diameter = 0.51
        data.seeding = 0.62
        data.shoulder = 0.83
        res.data = data
    except Exception as e:
        res.error(Error.SERVER_EXCEPTION)
        logger.error(e)
    return res


def total_normal_disb(res: ResponseBase):
    try:
        data = RespNormalDisb()
        
        res.data = data
    except Exception as e:
        res.error(Error.SERVER_EXCEPTION)
        logger.error(e)
    return res
