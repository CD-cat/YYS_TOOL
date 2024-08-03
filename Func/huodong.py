import adb,random
from time import sleep

from Func.base import keep_find
from Func.point_zb import *




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