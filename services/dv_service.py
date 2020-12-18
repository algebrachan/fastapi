from common.entity import ResponseBase, Error
from common.response import *
from utils.log import logger


def total_count(res: ResponseBase):
    try:
        data = RespGetTotalCount()
        data.diameter = CommonCount(1, 2, 3, 4)
        data.shoulder = CommonCount(5, 6, 7, 8)
        res.data = data
        1/0
    except Exception as e:
        res.error(Error.SERVER_EXCEPTION)
        logger.error(e)
    return res
