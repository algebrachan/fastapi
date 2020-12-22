import requests
from threading import Timer
import time
# 转换字典为对象


class Dict(dict):
    __setattr__ = dict.__setitem__
    __getattr__ = dict.__getitem__


def dict2obj(dictObj):
    if not isinstance(dictObj, dict):
        return dictObj
    d = Dict()
    for k, v in dictObj.items():
        d[k] = dict2obj(v)
    return d


def fun():
    r = requests.get('http://10.50.63.63:5000/daily_detection')
    res = dict2obj(r.json())
    localtime = time.asctime( time.localtime(time.time()) )
    print ("本地时间为 :", localtime)
    global t
    t = Timer(5.0,fun)
    t.start()

if __name__ == 'request':
    t = Timer(10.0,fun)
    t.start()

