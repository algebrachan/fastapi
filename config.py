from sqlalchemy import create_engine  # 建立数据库引擎
from sqlalchemy.orm import sessionmaker  # 建立回话session
from models.models import Base

db_user = 'root'
db_pwd = '123456'
db_host = '127.0.0.1'
db_port = '3306'
db_name = 'demo'

db_connect_string = 'mysql+pymysql://{0}:{1}@{2}:{3}/{4}?charset=utf8'.format(
    db_user, db_pwd, db_host, db_port, db_name)
engine = create_engine(db_connect_string, echo=True, max_overflow=5)  # 创建引擎
db_session = sessionmaker(bind=engine)  # 产生会话

def init_db():  # 根据类创建数据库表
    print('db init')
    Base.metadata.create_all(engine)


if __name__ == '__main__':
    
    init_db()
