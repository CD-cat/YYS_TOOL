import adb
from time import sleep
from Func.base import keep_find,keep_find_slow, keep_find_multiple
from Func import base,GetIn,untitled,base,jiejie
from Func.point_zb import *
import json,time
import redis

# with open("./data/game_data/base_arg.txt", "r") as f:  # 打开文件
#     data = f.read()  # 读取文件
#     base_arg = json.loads(data)

r = base.r
base_delay = float(r.get('base_delay').decode('utf-8'))


def Huijuan_Auto(time = 10):
    jiejie.jiejie()
    r.set('Tupojuan', 0)
    keep_find('SSL_main')
    GetIn.getin_tansuo()
    for i in range(time):
        if int(r.get('Tupojuan')) >20:
            point, pic_name = keep_find_multiple(['tansuo_yuhun', 'KUN28_Tansuo'])
            if pic_name == 'KUN28_Tansuo':
                adb.click(*KUN28_Back)
            else:
                pass
            point = keep_find('tansuo_jiejie')
            adb.click(*point)
            sleep(base_delay)
            jiejie.jiejie_fight(4)
            sleep(base_delay * 2)
            adb.click(*Btn_exit_jiejie)
            r.set('Tupojuan', 0)
        else:
            Kun28()
    sleep(base_delay*2)
    point, pic_name = keep_find_multiple(['tansuo_yuhun', 'KUN28_Tansuo'])
    if pic_name == 'KUN28_Tansuo':
        adb.click(*KUN28_Back)
    sleep(base_delay)
    adb.click(*Btn_Back)



def Kun28():
    # keep_find('tansuo_yuhun')  # 确定在这个界面
    point, pic_name = keep_find_multiple(['tansuo_yuhun', 'KUN28_Tansuo'])
    if pic_name == 'KUN28_Tansuo':
        adb.click(*point)
    else:
        adb.click(*KUN28_ZB)
        point = keep_find('KUN28_Tansuo')
        adb.click(*point)

    flag = True
    sleep(base_delay*2)
    while flag:
        point = adb.match('KUN28_Boss')
        if point != None:
            flag = False
            adb.click(*point)
            sleep(base_delay)
            point = keep_find('Fin_001')
            point1 = adb.match('tupojuan')
            if point1 != None:
                r.set('Tupojuan', int(r.get('Tupojuan')) + 1)
            adb.click(*point)
            sleep(base_delay*4)
            while True:
                point = adb.match('KUN28_Baoxiang')
                if point != None:
                    adb.click(*point)
                    sleep(base_delay)
                    point1 = adb.match('tupojuan')
                    if point1 != None:
                        r.set('Tupojuan', int(r.get('Tupojuan')) + 1)
                    adb.click(*tiaozhan)
                    sleep(1)
                else:
                    break


        else:
            point = adb.match('KUN28')
            if point != None:
                adb.click(*point)
                sleep(base_delay)
                point = adb.match('KUN28')
                if point != None:pass
                else:
                    point = keep_find('Fin_001')
                    point1 = adb.match('tupojuan')
                    if point1 != None:
                        r.set('Tupojuan',int(r.get('Tupojuan'))+1)
                    adb.click(*point)
                    sleep(base_delay*2)
            else:
                adb.swipe(1744, 2000, 800, 2000, 210)

        pass