from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

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
    id =Column(Integer,primary_key=True)
    name = Column(String(32))


