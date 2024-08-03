import adb,json
from time import sleep
import time,redis
from Func.point_zb import duiwu_coord,SSL_TZB_exit,\
    SSL_TZB_30,SSL_fenzu,Btn_Huahezhan,Btn_Back,\
    main_juanzhou,Btn_Huahezhan_Renwu
# from Func.point_zb import *
debug = True
# debug = False


r = redis.StrictRedis(host='localhost', port=6379, db=0)
base_delay = float(r.get('base_delay').decode('utf-8'))

def save_img (n):

    # adb.sc()
    if debug :print('777')
    # adb.device_check()
    # adb.sc()
    if n:
        n = n+'.png'
        adb.save_sc(n)
    else:
        adb.save_sc()
    if debug:print(n)
    if debug:print('666')


def huahezhan():
    while True:

        point = adb.match('SSL_main')
        if point != None:
            adb.click(*Btn_Huahezhan)
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
    sleep(base_delay*2)
    adb.click(*Btn_Huahezhan_Renwu)
    point = adb.match('Huahezhan_Lingqu')
    if point != None:
        adb.click(*point)
        sleep(base_delay)
        adb.click(*point)
    else:pass
    sleep(base_delay)
    adb.click(*Btn_Back)




# adb.save_sc('asd.png')
# save_img('asd.png')
def start_yys(): #打开阴阳师，坐标可用，模拟器打开首页的第二行第三个
    adb.click(440,946)

def enter_game():#进入游戏
    adb.click(950,850)

def close_new_card():#新式神：1750，200；珍藏皮、绝版皮：1800，150；
    adb.click(1750,200)

#式神录预设界面-切换对应预设阵容
def SSL_switch(fenzu,duiwu):
    sleep(base_delay * 3)
    point = keep_find('SSL_Yushe')
    adb.click(*point)
    sleep(base_delay)
    adb.swipe(1744,215,1744,825,210)#将分组拉到最上
    # pin_name = 'Auto'+str(fenzu)
    # point = keep_find('Auto'+str(fenzu))
    sleep(base_delay)
    adb.click(*SSL_fenzu[fenzu])
    sleep(base_delay)
    # if duiwu == 1:
    #     point = duiwu1
    # elif duiwu == 2:
    #     point = duiwu2
    # elif duiwu == 3:
    #     point = duiwu3
    adb.click(*duiwu_coord[duiwu-1])
    sleep(base_delay)
    point = adb.match('Confirm_Btn')
    if point != None:
        adb.click(*point)
    else:
        pass
    adb.click(*Btn_Back)

#式神录音频拓展包弹窗处理
def SSL_Deal_tuozhan():
    keep_find('SSL_Yushe')
    sleep(3)
    point = adb.match('SSL_downloadORnot')  # 寻找弹窗标志-是否下载
    if point != None:
        adb.click(*SSL_TZB_30)
        sleep(0.4)
        adb.click(*SSL_TZB_exit)
    else:
        pass


def cv_test(name):
    adb.match(name)


def keep_find(pic_name):
    # if debug :print(pic_name)
    point = None
    for i in range(100):
        point = adb.match(pic_name)
        if point != None:return point
        sleep(1)
        pass
    return point

def keep_find_slow(pic_name):
    # if debug: print(pic_name)
    point = None
    for i in range(100):
        point = adb.match(pic_name)
        if point != None: return point
        sleep(5)
        pass
    return point

def keep_find_multiple(pic_name_list):
    # if debug: print(pic_name_list)
    point = None
    for i in range(100):
        if type(pic_name_list) == str:
            point = adb.match(pic_name_list)
            if point != None: return point, pic_name_list
            pass
        else:
            for pic_name in pic_name_list:
                point = adb.match(pic_name)
                if point != None: return point, pic_name
                pass
        sleep(1)
    return point,'empty'

def keep_find_multiple_slow(pic_name_list):
    # if debug: print(pic_name_list)
    point = None
    for i in range(100):
        # str1 = type(pic_name_list)
        if type(pic_name_list) ==  str :
            point = adb.match(pic_name_list)
            if point != None: return point, pic_name_list
            pass
        else:
            for pic_name in pic_name_list:
                point = adb.match(pic_name)
                if point != None:return point,pic_name
                pass
        sleep(8)
    return point,'empty'

#每日更新log并转历史
def clear_log():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
    today = time.strftime('%Y-%m-%d', time.localtime())
    weekday = time.strftime('%w', time.localtime())
    # with open("./data/game_data/log_fight.txt", "r") as f:  # 打开文件
    #     data = f.read()  # 读取文件
    #     print(data)
    data = r.get('log_fight').decode('utf-8')
    fight_log = json.loads(data)
    if fight_log['date'] != today:
        # 记log
        fight_log_str = json.dumps(fight_log)
        with open('./data/game_data/log_fight_his.txt', 'r+', encoding='utf-8') as f:
            content = f.read()
            f.seek(0, 0)
            f.write(fight_log_str + '\n' + content)
        # 清零
        r.lpush('log_fight_his', fight_log_str)
        for i in fight_log:
            # if i == 'date':continue
            fight_log[i] = [0, 0]
        fight_log['date'] = today
        fight_log['weekday'] = weekday
        print(fight_log)

        # region 更新每日任务列表
        data = r.get('Task_List').decode('utf-8')
        Task_list = json.loads(data)
        for i in Task_list:
            Task_list[i] = [1, 0]
        # Task_list['digui'] = [0, 0] #胧车期间需要手动打极地鬼，暂时封禁自动地鬼
        if int(weekday) not in (5,6,0):
            Task_list['yinjie'] = [0, 0]
        Task_list_str = json.dumps(Task_list)
        r.set('Task_List',Task_list_str)
        # endregion

    fight_log_str = json.dumps(fight_log)
    r.set('log_fight',fight_log_str)
    # with open("./data/game_data/log_fight.txt", "w") as f:  # 打开文件
    #     f.write(fight_log_str)