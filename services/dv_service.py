from common.entity import ResponseBase, Error
from common.response import *


def total_count(res: ResponseBase):
    data = ApiGetTotalCount()
    data.diameter = CommonCount(1, 2, 3, 4)
    data.shoulder = CommonCount(5, 6, 7, 8)
    res.error(Error.NO_DATA)
    res.data = data
    return res
