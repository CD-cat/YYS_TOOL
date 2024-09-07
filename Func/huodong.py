import adb,random
from time import sleep

from Func.base import keep_find,base_delay,r,SSL_switch
from Func.point_zb import *


def huodong():
    while True:

        point = adb.match('SSL_main')
        if point != None:
            adb.click(*point)
            break
        else:
            adb.click(*main_juanzhou)  # 处理主界面挂机太久需要点返回的情况
            point = adb.match('SSL_main')
            if point != None:
                adb.click(*point)
                break
            else:
                adb.click(*Btn_Back)
                pass
        sleep(base_delay)
    SSL_switch(1, 4)
    keep_find('SSL_main')
    adb.click(*Huodong_point)
    keep_find('Btn_Back_Huodong')
    sleep(base_delay*2)
    adb.click(*Huodong_point_Sec)
    huodong_time = int(r.hget('Huodong', 'time'))
    huodong_number = int(r.hget('Huodong', 'number'))
    huodong_finish = int(r.hget('Huodong', 'finish'))
    fight_number = (huodong_number - huodong_finish)
    flag = huodong_fight(huodong_time, fight_number)
    huodong_number = int(r.hget('Huodong', 'number'))
    r.hset('Huodong', 'number', huodong_number + 1)
    if flag:
        pass
    else:
        adb.click(*tiaozhan)
        sleep(base_delay)
    point = keep_find('Btn_Back_Huodong')
    adb.click(*point)
    sleep(base_delay)
    adb.click(*point)
    sleep(base_delay)

    pass


# region 活动方法，由zhounian更改而来
def huodong_fight(time, need=50):
    if need > 200: need = 200
    # global x1, x2, y1, y2
    # startpoint = (x1 + 1300, y1 + 700)
    error_flag = False
    now = 0
    print('总计需要战斗：' + str(need) + '次')
    while True:
        keep_find('Btn_Back_Huodong')
        now += 1
        # x,y = tiaozhan
        # adb.click(x,y)
        adb.click(*tiaozhan)
        sleep(base_delay)
        point = adb.match('Btn_Back_Huodong')
        if point is not None:
            error_flag = True
            break
        # pyautogui.click(1566,831)
        if debug: print('开始第', now, '次战斗')

        sleep(int(time))
        # n = random()
        # if debug:print('随机数为：', n)
        # time.wait(n * 5)
        # find_and_click('overpc',waittime=3)
        point = keep_find('Fin_001')
        huodong_finish = int(r.hget('Huodong', 'finish'))
        r.hset('Huodong', 'finish', huodong_finish + 1)
        adb.click(*point)
        # sleep(5)
        # adb.click(x,y)
        if now == need:
            break
    if debug:
        if error_flag:
            print('战斗异常结束')
            r.hset('Huodong', 'flag', 0)
            return False
        else:
            print('活动战斗结束')
            return True


# endregion

# region 最早的手动活动方法，最开始为了周年庆开发的
def zhounian(time,need = 50):
    # global x1, x2, y1, y2
    # startpoint = (x1 + 1300, y1 + 700)
    now = 0
    print('总计需要战斗：'+str(need)+'次')
    while True:
        now += 1
        x,y = tiaozhan
        # adb.click(x,y)
        adb.click(*tiaozhan)
        # pyautogui.click(1566,831)
        if debug:print('开始第', now, '次战斗')

        sleep(int(time))
        # n = random()
        # if debug:print('随机数为：', n)
        # time.wait(n * 5)
        # find_and_click('overpc',waittime=3)
        point = keep_find('Fin_001')
        adb.click(*point)
        # sleep(5)
        # adb.click(x,y)
        if now == need:
            break
        sleep(3)

    if debug:print('战斗结束')