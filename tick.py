# 轮询函数
import requests
from threading import Timer
import time
from services.sql_service import add_diameter_detection_result

interval = 60.0*60 # 1小时轮询


def tick():
    # 定时执行一些请求
    add_diameter_detection_result()
    localtime = time.asctime(time.localtime(time.time()))
    print("本地时间为 :", localtime)
    global t
    t = Timer(interval, tick)
    t.start()


if __name__ == 'tick':
    t = Timer(interval, tick)
    t.start()
