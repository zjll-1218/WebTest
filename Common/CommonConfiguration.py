# coding=utf-8
from datetime import datetime


def baseUrl():
    return 'http://192.168.10.93:12304/login.html'


def getCurrentTime():
    # 格式化当前时间
    format = "%a %b %d %H:%M:%S %Y"
    return datetime.now().strftime(format)


def timeDiff(starttime, endtime):
    # 计算时间差
    format = "%a %b %d %H:%M:%S %Y"
    return datetime.strftime(endtime, format) - datetime.strftime(starttime, format)

