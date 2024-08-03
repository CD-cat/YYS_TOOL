


import adb,random
from time import sleep
from Func.base import keep_find,keep_find_slow
from Func import base
from Func.point_zb import *


#探索
def getin_tansuo():
    adb.click(*tansuo)
#御魂
def getin_yuhun(hun):
    getin_tansuo()
    point = keep_find('tansuo_yuhun')
    adb.click(*point)
    point = keep_find('yuhun_main')#御魂界面判断，魂火、混日、魂海直接在下面点击对应坐标即可
    adb.click(*yuhun[hun])
#结界
def getin_jiejie():
    getin_tansuo()
    point = keep_find('tansuo_jiejie')
    adb.click(*point)
#委派
def getin_Weipai():
    getin_tansuo()
    point = keep_find('tansuo_weipai')
    adb.click(*point)
