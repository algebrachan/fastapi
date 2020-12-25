from common.entity import ResponseBase, Error
from common.response import *
from config import db_session
from sqlalchemy import and_
from models.models import DetectionResult
from utils.log import logger
from datetime import datetime, date
from services.sql_service import get_one_detection_result, get_history_broken_nums
import random


def total_count(res: ResponseBase):

    data = RespGetTotalCount()
    try:
        logger.info('get total')
        # 获取当前的时间字符串
        datenow = datetime.now().date()
        db_shoulder = get_one_detection_result(datenow, 1)
        db_diameter = get_one_detection_result(datenow, 2)
        data.shoulder = (CommonCount(0, 0, 0, 0) if (db_shoulder == None) else CommonCount(
            db_shoulder.dev_nums, db_shoulder.broken_nums, db_shoulder.fp_nums, db_shoulder.fn_nums))
        data.diameter = (CommonCount(0, 0, 0, 0) if (db_diameter == None) else CommonCount(
            db_diameter.dev_nums, db_diameter.broken_nums, db_diameter.fp_nums, db_diameter.fn_nums))
    except Exception as e:
        res.error(Error.SERVER_EXCEPTION)
        logger.error(e)
        pass
    res.data = data
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
        for i in get_history_broken_nums(1, 10):
            item = CommonListItem(i.date.strftime('%m-%d'), i.broken_nums)
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
        data.total = 400
        data.rate = round(data.succ/data.total, 4)
        for i in ['1', '3', '5', '7', '9', '11']:
            item = CommonListItem(i, random.randint(1, 100))
            data.distribution.append(item)
        for i in get_history_broken_nums(2, 10):
            item = CommonListItem(i.date.strftime('%m-%d'), i.broken_nums)
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
