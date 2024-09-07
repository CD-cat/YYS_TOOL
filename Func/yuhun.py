import json,redis
from time import sleep

import adb
from Func import base, GetIn
from Func.base import keep_find_multiple, keep_find
from Func.point_zb import main_juanzhou, Btn_Back, yuhun_team, yuhun_dashe, Btn_jiacheng, jiacheng, tiaozhan
from Func.richang import base_delay


def yuhun(hun):
    r = base.r
    while True:

        point = adb.match('SSL_main')
        if point != None:
            adb.click(*point)
            break
        else:
            adb.click(*main_juanzhou)       #处理主界面挂机太久需要点返回的情况
            point = adb.match('SSL_main')
            if point != None:
                adb.click(*point)
                break
            else:
                adb.click(*Btn_Back)
                pass
        sleep(base_delay)
    base.SSL_switch(*yuhun_team[hun])
    if hun == 'shui':
        sleep(base_delay)
        adb.click(*point)
        base.SSL_switch(4,2)
    sleep(3 * base_delay)
    GetIn.getin_yuhun(hun)
    sleep(base_delay)
    adb.swipe(480, 825, 480, 215, 210)
    adb.click(*yuhun_dashe[hun])
    if hun in ('tu','wang','shi'):
        adb.click(*Btn_jiacheng)
        sleep(base_delay)
        adb.click(*jiacheng[1])
        sleep(base_delay)
        adb.click(*Btn_jiacheng)
        sleep(base_delay)
        pass

    with open("./data/game_data/log_time.txt", "r") as f:  # 打开文件
        data = f.read()  # 读取文件
        global time_log
        time_log = json.loads(data)
    with open("./data/game_data/log_fight.txt", "r") as f:  # 打开文件
        data = f.read()  # 读取文件
        print(data)
    data = r.get('log_fight')
    fight_log = json.loads(data)
    sleep(base_delay)




    with open("./data/game_data/yuhun_time.txt", "r") as f:  # 打开文件
        data = f.read()  # 读取文件
        print(data)
    fight_time = json.loads(data)
    f_time = fight_time[int(fight_log['weekday'])]

    for i in range(f_time):
        hun_fight(time_log[hun], 1)
        fight_log[hun][0] += 1
        fight_log_str = json.dumps(fight_log)
        r.set('log_fight',fight_log_str)
        with open("./data/game_data/log_fight.txt", "w") as f:  # 打开文件
            f.write(fight_log_str)

    sleep(base_delay)
    if hun in ('tu', 'wang','shi'):
        adb.click(*Btn_jiacheng)
        sleep(base_delay)
        adb.click(*jiacheng[1])
        sleep(base_delay)
        adb.click(*Btn_jiacheng)
        sleep(base_delay)
        pass
    adb.click(*Btn_Back)
    sleep(base_delay)
    adb.click(*Btn_Back)

    pass


def hun_fight(time, need = 30):
    # adb.click(*tansuo)
    # point = keep_find('tansuo_yuhun')
    # adb.click(*point)
    # point = keep_find('yuhun_main')#御魂界面判断，魂火、混日、魂海直接在下面点击对应坐标即可
    # adb.click(*point)
    # point = keep_find('SSL_Yushe')
    # adb.click(*point)
    # GetIn.getin_yuhun('tu')
    now = 0
    while now < need:
        now += 1
        sleep(base_delay)
        adb.click(*tiaozhan)
        # if debug:print('开始第', now, '次战斗')
        sleep(int(time))
        # point, pic_name = keep_find_multiple(['Fin_004','Fin_001','Fin_003'])
        point, pic_name = keep_find_multiple(['Fin_004', 'Fin_001'])
        if pic_name ==  'Fin_001':
            adb.click(*point)
        else:
            x, y = point
            adb.click(x-268,y)
            point = keep_find('Fin_001')
            adb.click(*point)
        sleep(base_delay)
        # if now == need:
        #     break


    # if debug:print('战斗结束')