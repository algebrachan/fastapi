from typing import List
from enum import Enum, unique
from pydantic import BaseModel, Schema, Field


@unique
class Error(Enum):
    UNKNOWN = -1
    SUCCESS = 0
    NO_DATA = 1
    SERVER_EXCEPTION = 4
    NO_AUTH = 5


dict_error = {
    'UNKNOWN': '未知错误',
    'SUCCESS': '请求成功',
    'NO_DATA': '没有数据',
    'SERVER_EXCEPTION': '服务器异常',
    'NO_AUTH': '没有权限'
}


class RequestBase(BaseModel):
    token: str = ""
    limit: int = None


class ResponseBase(BaseModel):
    code: int = 0
    msg: str = "请求成功"
    data: dict = {}

    def error(self, err_code: Error):
        self.code = err_code.value
        self.msg = dict_error[err_code.name]
        # error枚举类
