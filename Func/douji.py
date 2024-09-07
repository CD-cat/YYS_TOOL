import json,redis
from time import sleep
from Func.richang import base_delay
import adb
from Func.base import keep_find, keep_find_multiple_slow
from Func.point_zb import douji_fight, douji_zidong_up, douji_auto_fight
from Func import base


def douji():
    r = base.r
    with open("./data/game_data/log_fight.txt", "r") as f:  # 打开文件
        data = f.read()  # 读取文件
        print(data)
    data = r.get('log_fight').decode('utf-8')
    fight_log = json.loads(data)

    point = adb.match('Fin_001')  # 处理胜利次数奖励
    if point != None:
        adb.click(*douji_fight)
    else:
        pass
    sleep(base_delay)
    point = adb.match('douji_levelup')  # 处理挑战卷不足的情况
    if point != None:  # 如果攻打按钮还在，
        adb.click(*douji_fight)
    else:
        pass


    keep_find('douji_duanwei')#是否使用keepfind有待商榷
    adb.click(*douji_fight)
    sleep(base_delay*5)
    adb.click(*douji_zidong_up)
    sleep(base_delay * 8)
    # point = adb.match('douji_zengyi')
    # if point != None:
    #     adb.click(*douji_auto_fight)
    # else:
    #     sleep(base_delay*2)
    find_list = ['douji_fenxiang','Fin_005','Fin_fail','douji_zengyi','douji_duanwei']
    while True:
        point,picname =  keep_find_multiple_slow(find_list)
        if picname == 'douji_fenxiang':
            fight_log['douji'][0] += 1
            adb.click(*douji_zidong_up)
            point, picname = keep_find_multiple_slow('Fin_002')
            adb.click(*point)
            break
            # sleep(3)
        elif picname == 'Fin_fail':
            fight_log['douji'][1] += 1
            adb.click(*point)
            break
        elif picname == 'Fin_005':
            fight_log['douji'][0] += 1
            adb.click(*douji_zidong_up)
            break
        elif picname == 'douji_zengyi':
            adb.click(*douji_auto_fight)
            del find_list[-1]
        elif picname == 'douji_duanwei':
            return

    '''
        处理斗技升段/掉段弹窗√
        以及胜利次数奖励√
    '''
    sleep(base_delay*2)
    point = adb.match('Fin_001')  # 处理胜利次数奖励
    if point != None:
        adb.click(*douji_fight)
    else:
        pass
    sleep(base_delay)
    point = adb.match('douji_levelup')  # 处理挑战卷不足的情况
    if point != None:  # 如果攻打按钮还在，
        adb.click(*douji_fight)
    else:
        pass

    fight_log_str = json.dumps(fight_log)
    r.set('log_fight',fight_log_str)
    # with open("./data/game_data/log_fight.txt", "w") as f:  # 打开文件
    #     f.write(fight_log_str)


    pass