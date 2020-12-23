from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, TIMESTAMP
import time
# from config import Base
Base = declarative_base()


class Course(Base):
    __tablename__ = 'course'  # 定义该表在mydql数据库中的实际名称
    # 定义表的内容
    id = Column(Integer, primary_key=True)
    name = Column(String)
    subject = Column(String)


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(32))


class DetectionResult(Base):
    """detection result table

    param:key - primary_key 
    param:date 日期标记
    param:dev_nums 当前在线检测炉台数量
    param:broken_nums 当日检出断苞异常数量
    param:fp_nums 等径误检数量
    param:fn_nums 等径漏检数量
    param:update_time 操作时间
    param:type 1-放肩 2-等径
    """
    __tablename__ = 'detection_result'
    key = Column(Integer, primary_key=True, autoincrement=True)
    date = Column(Date, nullable=False, default='0000-00-00')
    dev_nums = Column(Integer, nullable=False, default=0)
    broken_nums = Column(Integer, nullable=False, default=0)
    fp_nums = Column(Integer, nullable=False, default=0)
    fn_nums = Column(Integer, nullable=False, default=0)
    update_times = Column(Integer, nullable=False, default=0)
    type = Column(Integer, nullable=False, default=0)

    def setData(self, data: object, type: int):
        self.date = data.date
        self.dev_nums = data.device_nums
        self.broken_nums = data.bronken_nums
        self.fp_nums = data.fp_nums
        self.fn_nums = data.fn_nums
        self.update_times = int(time.time())
        self.type = type
