# resp开头的类为 响应类

class RespGetTotalCount:
    """
    获取总计数据 响应类
    """
    shoulder: dict
    diameter: dict

    def __init__(self):
        self.shoulder = {}
        self.diameter = {}


class CommonCount:
    """总计数据 结构
    """
    online: int  # 在线检测数量
    brek: int  # 检出断苞数量
    fail: int  # 误检数量
    miss: int   # 漏检数量

    def __init__(self, online, brek, fail, miss):
        self.online = online 
        self.brek = brek 
        self.fail = fail 
        self.miss = miss 


class CommonListItem:
    """ 图表类 通用item
    """
    item: str  # 分类的item
    value: int  # 暂时定义为int类型

    def __init__(self, item, value):
        self.item = item
        self.value = value


class RespGetSeriesCount:
    """系列数据 响应类
    """
    shoulder: list
    diameter: list

    def __init__(self):
        self.shoulder = []
        self.diameter = []


class RespTotalShoulderData:
    """获取放肩总计数据 响应类
    """
    succ: int  # 成功数量
    total: int  # 总计数量
    rate: float  # 比例
    distribution: list  # 分布
    history: list  # 历史数据

    def __init__(self):
        self.succ = 0
        self.total = 0
        self.rate = 0.0
        self.distribution = []
        self.history = []


class RespTotalDiameterData(RespTotalShoulderData):  # 继承的写法
    def __init__(self):
        super().__init__()


class RespTotalRates:
    accuracy: float  # 熔接功率预测准确率
    seeding: float  # 引晶受控占比
    shoulder: float  # 放肩受控占比
    diameter: float  # 等径受控占比

    def __init__(self):
        self.accuracy = 0.0
        self.seeding = 0.0
        self.shoulder = 0.0
        self.diameter = 0.0


class RespNormalDisb:
    stable_time: list  # 稳温工时，熔接-引晶开始的时间 分布函数，例：2h - 200  time - count 一次工艺过程
    seeding_speed: list  # 引晶完成的晶体速率 例 2cm/s - 100  s - count
    shoulder_len: list  # 放肩长度 len - count
    average_s: list  # 取断收尾，晶体长度/工艺时间 = 平均拉速

    def __init__(self):
        self.stable_time = []
        self.seeding_speed = []
        self.shoulder_len = []
        self.average_s = []
