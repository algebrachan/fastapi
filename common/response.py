# api开头的类为 响应类

class ApiGetTotalCount:
    shoulder: dict = {}
    diameter: dict = {}


class CommonCount:
    online: int = 0  # 在线检测数量
    brek: int = 0  # 检出断苞数量
    fail: int = 0  # 误检数量
    miss: int = 0  # 漏检数量

    def __init__(self, online, brek, fail, miss):
        self.online = online
        self.brek = brek
        self.fail = fail
        self.miss = miss
