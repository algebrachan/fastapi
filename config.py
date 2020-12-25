from sqlalchemy import create_engine  # 建立数据库引擎
from sqlalchemy.orm import sessionmaker  # 建立回话session
from models.models import Base, DetectionResult
import time
from datetime import datetime, date

db_user = 'root'
db_pwd = '123456'
db_host = '127.0.0.1'
db_port = '3306'
db_name = 'demo'

db_connect_string = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(
    db_user, db_pwd, db_host, db_port, db_name)
engine = create_engine(db_connect_string, max_overflow=5)  # 创建引擎 echo=True 打印日志
db_session = sessionmaker(bind=engine)  # 产生会话


def init_db():  # 根据类创建数据库表
    print('db init')
    # Base.metadata.create_all(engine)
    # print(str(datetime.now().date()))
    # print(int(time.time()))
    # str -> date
    # detester = '2017-01-01'
    # date = datetime.strptime(detester, '%Y-%m-%d')
    # print(date)
def test():
    session = db_session()
    dr = DetectionResult()
    session.add(dr)
    session.commit()

# 创建表的时候执行
if __name__ == '__main__':
    init_db()