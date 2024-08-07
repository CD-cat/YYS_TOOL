from time import sleep

import adb,datetime
from Func import base
from Func.base import keep_find, keep_find_slow
from Func.point_zb import fengmo_foxiang, fengmo_richang, fengmo_entry, tiaozhan, fengmo_damo, fengmo_boss_quit, \
    fenghmo_cent, Btn_Back, fengmo_xianshi, fengmo_lanpiao, fengmo_quit
from Func.richang import base_delay

#逢魔



def fengmo():
    # adb.swipe(1744, 215, 1744, 825, 210)  # 将分组拉到最上
    adb.swipe(800, 2000, 1744, 2000, 210)
    adb.swipe(800, 2000, 1744, 2000, 210)
    adb.swipe(800, 2000, 1744, 2000, 210)
    adb.click(*fengmo_foxiang)
    sleep(base_delay)
    adb.click(*fengmo_richang)
    sleep(base_delay)
    adb.click(*fengmo_entry)

    # point = keep_find('fengmo_entry')
    # adb.click(*point)
    # keep_find('fengmo_entry2')
    # adb.click(*fengmo_entry)

    #加一个延时
    sleep(base_delay)
    point = adb.match('fengmo_ji')#处理封魔·极弹窗
    if point != None:
        adb.click(*point)
    else:
        pass
    sleep(base_delay)
    #region 现世逢魔&达摩
    for i in range(5):
        adb.click(*tiaozhan)
        sleep(base_delay*5)
    adb.click(*fengmo_damo)
    sleep(base_delay)
    adb.click(*fengmo_damo)
    sleep(base_delay)
    find_lanpiao()

    #endregion

    sleep(3.14)
    point = keep_find('SSL_logo')
    adb.click(*point)

    week_day = datetime.datetime.now().isoweekday()
    if week_day == 4:
        base.SSL_switch(2, 3)
    else:
        base.SSL_switch(2, 2)
    x,y = point
    # region 确认是否进入逢魔集结界面
    while True:
        point = adb.match('SSL_fengmo')
        if point != None:
            break
        else:
            pass
        point = adb.match('Btn_jijieFight')
        if point != None:
            adb.click(*fengmo_boss_quit)
        else:
            pass

        adb.click(x+158,y)#偏移量
        sleep(0.8)
        adb.click(*fenghmo_cent)
        sleep(0.8)
        adb.click(*tiaozhan)
        sleep(9.58)
    # endregion
    while True:
        point = adb.match('SSL_fengmo')
        if point != None:
            pass
        else:
            break
    sleep(6.66)
    keep_find_slow('Btn_back')#不能用这个表示，得找组图表
    adb.click(*tiaozhan)
    sleep(360.12)
    keep_find_slow('SSL_logo')
    sleep(base_delay)
    adb.click(*Btn_Back)
    '''
    这里想办法如何快速识别逢魔首领并进入
    '''
    '''
    进入以后，多次寻找组字，然后开始战斗
    然后慢找式神录，退出
    '''

#逢魔宝箱找蓝票
def find_lanpiao():
    for i in range(4):
        adb.click(*fengmo_xianshi[i])
        sleep(base_delay)
        point = adb.match('Fengmo_Guiwang')
        if point != None:  # 如果攻打按钮还在，
            point = adb.match('Fengmo_Guiwang_Fight')
            if point != None:  # 如果攻打按钮还在，
                adb.click(*point)
                keep_find_slow('SSL_logo')

            else:
                adb.click(*fengmo_boss_quit)
                pass
        else:
            point = adb.match('lanpiao')  # 处理挑战卷不足的情况
            if point != None:  # 如果攻打按钮还在，
                adb.click(*fengmo_lanpiao)
            else:
                sleep(base_delay)
                adb.click(*fengmo_quit)
                sleep(base_delay)
                point = adb.match('SSL_logo')  # 如果没有回到逢魔界面，即为进入了战斗
                if point != None:  # 如果攻打按钮还在，
                    pass
                else:
                    adb.click(*tiaozhan)
                    point = keep_find_slow('Fin_001')
                    adb.click(*point)
                    '''
                            找buff标志，判断是否进入战斗
                            找fin——001，点击
                    '''
        sleep(base_delay)
