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
    # jiejie_fight(4)
    ka_flag = int(r.hget('Task_Flag','jiejie'))
    if ka_flag :
        jiejie_fight_V3(4,ka_flag)
    else:
        jiejie_fight_non(4)
    sleep(base_delay*2)
    adb.click(*Btn_exit_jiejie)
    sleep(base_delay*2)
    adb.click(*Btn_Back)
    # sleep(base_delay)


# region 结界突破 Ver3.0第二版卡57
def jiejie_fight_V3(need = 1,ka_time = 1):
    end_flag = False

    for j in range(need):
        if end_flag: break

        for i in range(9):
            keep_find('jiejie_main')  # 确定在结界突破界面
            adb.click(*jiejie_point[i])
            sleep(base_delay)
            point = adb.match('jiejie_attack')
            if point != None:  # 如果有攻打按钮
                adb.click(*point)
            else:
                continue
            sleep(base_delay)
            point = adb.match('jiejie_attack')  # 处理挑战卷不足的情况
            if point != None:  # 如果攻打按钮还在，
                # adb.click(*point)
                end_flag = True
                adb.click(*Btn_Back)
                break
            else:
                pass
            if i == 0:
                point = keep_find('Btn_back')
                adb.click(*point)

                point = keep_find('jiejie_renshu_confirm')
                adb.click(*point)
                sleep(base_delay * 2)
                adb.click(*tiaozhan)

                if ka_time > 1:
                    Ka57(ka_time-1)
                sleep(base_delay * 2)
                adb.click(*jiejie_point[i])
                sleep(base_delay)
                point = adb.match('jiejie_attack')
                if point != None:  # 如果有攻打按钮
                    adb.click(*point)
                else:
                    continue
            point = keep_find('Btn_back')
            adb.click(*tiaozhan)
            sleep(base_delay)
            point = keep_find_slow('Fin_001')
            adb.click(*point)
            sleep(base_delay*3)
            point = adb.match('Fin_001')
            if point != None:
                adb.click(*point)
            else:
                pass



# endregion


def Ka57(time):
    for k in range(time):
        keep_find('jiejie_main')  # 确定在结界突破界面
        adb.click(*jiejie_point[8])
        sleep(base_delay)
        point = adb.match('jiejie_attack')
        if point != None:  # 如果有攻打按钮
            adb.click(*point)

        else:
            continue
        sleep(base_delay)
        point = adb.match('jiejie_attack')  # 处理挑战卷不足的情况
        if point != None:  # 如果攻打按钮还在，
            # adb.click(*point)
            end_flag = True
            adb.click(*Btn_Back)
            break
        else:
            pass
        sleep(base_delay)
        point = keep_find('Btn_back')
        adb.click(*point)

        point = keep_find('jiejie_renshu_confirm')
        adb.click(*point)
        sleep(base_delay * 2)
        adb.click(*tiaozhan)

# region 结界突破 战斗模块Ver1.0 不卡等级
def jiejie_fight_non(need = 1):
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

            point = keep_find_slow('Fin_001')
            adb.click(*point)
            sleep(5)
            point = adb.match('Fin_001')
            if point != None:
                adb.click(*point)
            else:
                pass

# endregion



#结界突破 战斗模块Ver2.0，卡57级退四次，已被优化
def jiejie_fight(need = 1):
    end_flag = False

    for j in range(need):
        if end_flag : break
        for  k in range(4):
            keep_find('jiejie_main')  # 确定在结界突破界面
            adb.click(*jiejie_point[8])
            sleep(base_delay)
            point = adb.match('jiejie_attack')
            if point != None:  # 如果有攻打按钮
                adb.click(*point)

            else:
                continue
            sleep(base_delay )
            point = adb.match('jiejie_attack')  # 处理挑战卷不足的情况
            if point != None:  # 如果攻打按钮还在，
                # adb.click(*point)
                end_flag = True
                adb.click(*Btn_Back)
                break
            else:
                pass
            sleep(base_delay)
            point = keep_find('Btn_back')
            adb.click(*point)

            point = keep_find('jiejie_renshu_confirm')
            adb.click(*point)
            sleep(base_delay*2)
            adb.click(*tiaozhan)



        for i in range(9):
            keep_find('jiejie_main')#确定在结界突破界面
            adb.click(*jiejie_point[i])
            sleep(base_delay)
            point = adb.match('jiejie_attack')
            if point != None:  # 如果有攻打按钮
                adb.click(*point)

            else:
                continue
            sleep(base_delay)
            point = adb.match('jiejie_attack')#处理挑战卷不足的情况
            if point != None:#如果攻打按钮还在，
                # adb.click(*point)
                end_flag = True
                adb.click(*Btn_Back)
                break
            else:
                pass
            point = keep_find('Btn_back')
            adb.click(*tiaozhan)
            sleep(base_delay)
            point = keep_find_slow('Fin_001')
            adb.click(*point)
            sleep(5)
            point = adb.match('Fin_001')
            if point != None:
                adb.click(*point)
            else:
                pass

            # if i == 2:
            #     point = keep_find('jiejie_refresh')
            #     adb.click(*point)
            #     point = keep_find('jiejie_refresh_confirm')
            #     adb.click(*point)

