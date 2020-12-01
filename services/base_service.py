from config import db_session
from models.models import Course
from utils.log import logger
# 提交数据

def q_course():
    session = db_session()
    r0 = session.query(Course).all()
   
    # session.commit()

    session.close()
    return r0

def add_course():
    session = db_session()   
    session.add(Course(name="wc",subject="math"))
    session.commit() # 提交事务
    session.close()  # 关闭session