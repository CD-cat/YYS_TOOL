from time import sleep

import adb
from Func import base, GetIn
from Func.base import *
from Func.point_zb import *
from Func.richang import base_delay



#
def jiejie():
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
    base.SSL_switch(1,1)
    sleep(3 * base_delay)
    GetIn.getin_jiejie()
    sleep(base_delay)
    jiejie_fight(4)
    sleep(base_delay*2)
    adb.click(*Btn_exit_jiejie)
    sleep(base_delay*2)
    adb.click(*Btn_Back)
    # sleep(base_delay)


#结界突破 战斗模块
def jiejie_fight(need = 1):
    end_flag = False

    for j in range(need):
        if end_flag : break
        for i in range(9):
            # if i < 4 :continue
            keep_find('jiejie_main')#确定在结界突破界面
            adb.click(*jiejie_point[i])
            sleep(base_delay)
            point = adb.match('jiejie_attack')
            if point != None:  # 如果有攻打按钮
                adb.click(*point)

            else:
                continue
            sleep(base_delay*3)
            point = adb.match('jiejie_attack')#处理挑战卷不足的情况
            if point != None:#如果攻打按钮还在，
                # adb.click(*point)
                end_flag = True
                adb.click(*Btn_Back)
                break
            else:
                pass
            sleep(base_delay)
            # point = adb.match('jiejie_main') #确定在结界突破界面
            # if point != None:  # 如果攻打按钮还在，
            #     # adb.click(*point)
            #
            #     continue
            # else:
            #     pass

            # point = adb.match('jiejie_dianzan')#结界点赞按钮，找得到点一下
            # if point != None:
            #     adb.click(*point)
            # else:
            #     pass
            point = keep_find_slow('Fin_001')
            adb.click(*point)
            sleep(5)
            point = adb.match('Fin_001')
            if point != None:
                adb.click(*point)
            else:
                pass