from typing import List

from pydantic import BaseModel, Schema, Field


class RequestBase(BaseModel):
    token: str = ""
    limit: int = None


class ResponseBase(BaseModel):
    code: int = 0
    msg: str = "请求成功"
    data: dict = {}
