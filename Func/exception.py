import redis
import adb
from time import sleep
from Func import untitled
from Func.richang import base_delay
from Func.point_zb import *
from Func.base import keep_find,keep_find_slow, keep_find_multiple


r = redis.StrictRedis(host='localhost', port=6379, db=0)
#region 异常处理
def deal_exception():
    error_flag = False
    #关闭加成
    sleep(base_delay)
    point = adb.match('yuhun_jiacheng_15m')
    if point != None:
        error_flag = True
        adb.click(*Btn_Yuhun_Jiacheng_Close)

    #周六第一次御魂自选，异常处理（后面加上御魂任务控制变量更改，以方便用户确认自选御魂）
    point = adb.match('yuhun_zixuan_flag')
    if point != None:
        error_flag = True
        adb.click(*Btn_Yuhun_Zixuan_Exit)
        sleep(base_delay)
        adb.click(*tiaozhan)
        sleep(base_delay)
        adb.click(*Btn_jiacheng)
        sleep(base_delay)
        adb.click(*jiacheng[1])
        sleep(base_delay)
        adb.click(*Btn_jiacheng)
        sleep(base_delay)
        adb.click(*Btn_Back)
        keep_find('tansuo_yuhun')
        adb.click(*Btn_Back)
        keep_find('SSL_main')
    return error_flag
#endregion

#region 异常处理不了，重启游戏
def restart():
    end_str = ['shell am force-stop com.netease.onmyoji','shell am force-stop com.netease.onmyoji.bili']
    key = adb.adb(end_str[int(r.get('Server_Switch'))])
    sleep(base_delay*10)
    untitled.open_YYS()
#endregion