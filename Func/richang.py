import adb
from time import sleep
from Func.base import keep_find,keep_find_slow, keep_find_multiple
from Func import base,GetIn,untitled
from Func.point_zb import *
import json,time
import redis

# with open("./data/game_data/base_arg.txt", "r") as f:  # 打开文件
#     data = f.read()  # 读取文件
#     base_arg = json.loads(data)

r = redis.StrictRedis(host='localhost', port=6379, db=0)
base_delay = float(r.get('base_delay').decode('utf-8'))
debug = True
# debug = False

def test ():

    key = adb.adb('shell am force-stop com.netease.onmyoji.bili')
    # key = adb.adb('shell am start -n com.netease.onmyoji.bili')
    untitled.open_YYS()
    # key = adb.adb('shell pm list packages')
    print(key)
    # r.close

#阴界之门
def yinjie():
    r = redis.StrictRedis(host='localhost', port=6379, db=0)
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
    base.SSL_switch(0,4)
    keep_find('SSL_main')
    adb.click(*Btn_YYL)
    point = keep_find('YYL_Shenshe')
    adb.click(*point)
    point = keep_find('YYL_Shenshe_Shoulie')
    adb.click(*point)
    point = keep_find('YYL_Yinjie_Entry')
    adb.click(*point)
    point = keep_find('YYL_Yinjie_Tiaozhan')
    adb.click(*point)
    point = keep_find('Confirm_Btn')
    adb.click(*point)
    point = keep_find('Btn_Xiezhan_Tiaozhan')
    adb.click(*point)
    keep_find('Fight_Ready')
    adb.click(*tiaozhan)
    sleep(base_delay*15)
    point = keep_find_slow('Fin_002')
    adb.click(*point)
    keep_find('YYL_Yinjie_Entry')
    adb.click(*Btn_Back)
    keep_find('YYL_Shenshe')
    adb.click(*Btn_Back)
    sleep(base_delay*2)



#阴阳寮金币领取
def liao_jinbi():
    while True:

        point = adb.match('SSL_main')
        if point != None:
            adb.click(*Btn_YYL)
            break
        else:
            adb.click(*main_juanzhou)  # 处理主界面挂机太久需要点返回的情况
            point = adb.match('SSL_main')
            if point != None:
                adb.click(*Btn_YYL)
                break
            else:
                adb.click(*Btn_Back)
                pass
        sleep(base_delay)
    point = keep_find('YYL_Xinxi')
    adb.click(*point)
    point = keep_find('YYL_Zijin')
    adb.click(*point)
    sleep(base_delay*2)
    point = adb.match('YYL_Zijin_Get')
    if point != None:
        adb.click(*point)
        sleep(base_delay*2)
        adb.click(*tiaozhan)
        sleep(base_delay)
    adb.click(*Btn_Back)
    point = keep_find('YYL_Xinxi')
    adb.click(*Btn_Back)


#结界寄养
def jiyang():
    back_flag = 0
    taigu_flag = 0
    while True:
        sleep(base_delay)
        point = adb.match('SSL_main')
        if point != None:
            adb.click(*Btn_YYL)
            break
        else:
            sleep(base_delay)
            adb.click(*main_juanzhou)  # 处理主界面挂机太久需要点返回的情况
            point = adb.match('SSL_main')
            if point != None:
                adb.click(*Btn_YYL)
                break
            else:
                adb.click(*Btn_Back)
                pass
        sleep(base_delay)
    point = keep_find('YYL_Jiejie')
    adb.click(*point)
    sleep(base_delay)
    while True:
        adb.click(*Btn_Jiejie_Yucheng)
        sleep(base_delay)
        point = adb.match('YYL_Jiejie_Yucheng')
        if point != None:break
    adb.click(*Btn_Jiejie_Jiyang)
    point,picname =keep_find_multiple(['jiyang_jinru','jiyang_chakan'])
    if picname == 'jiyang_chakan':
        # flag = False
        adb.click(*tiaozhan)
        back_flag = 2
        sleep(base_delay)
        adb.click(*Btn_Back)

    else:

        flag = True
        for i in range(20):
            point = adb.match('jiejieka_taigu_6', 0.93)  # 六星太古
            if point != None:
                flag = not flag
                taigu_flag = 6
            if flag:
                point = adb.match('jiejieka_taigu_5',0.98)#五星太鼓
                if point != None:
                    taigu_flag = 5
                    flag = not flag
            if flag:
                point = adb.match('jiejieka_taigu_4',0.98)#四星太古
                if point != None:
                    flag = not flag
                    taigu_flag = 4
            if flag:
                #下滑翻页循环
                adb.swipe(560, 825, 560, 715, 15)
                adb.click(560, 825)
                pass
            else:
                adb.click(*point)
                point = keep_find('jiyang_jinru')
                adb.click(*point)
                sleep(base_delay)
                keep_find('Flag_Shishen_yucheng')
                adb.click(*ZB_SSL_Kapian[0])
                point = keep_find('Jiyang_Confirm')
                adb.click(*point)
                back_flag = 1
                keep_find('Flag_Shishen_yucheng')
                adb.click(*Btn_Back)
                sleep(base_delay * 2)
                adb.click(*Btn_Back)
                break
            if i == 19:
                adb.click(*tiaozhan)
                back_flag = 3
                sleep(base_delay)
                adb.click(*Btn_Back)


    sleep(base_delay * 2)
    adb.click(*Btn_Back)
    keep_find('YYL_Jiejie')
    adb.click(*Btn_Back)
    return back_flag,taigu_flag
        # for i in ZB_Jiejie_Jiyang:
        #     adb.click(*i)
        #     sleep(base_delay)
        #     point = adb.match('jiejieka_taigu_5')#六星太古
        #     if point != None:
        #         flag = not flag
        #     if flag:
        #         point = adb.match('jiejieka_taigu_5')#五星太鼓
        #         if point != None:
        #             flag = not flag
        #     if flag:
        #         point = adb.match('jiejieka_taigu_5')#四星太古
        #         if point != None:
        #             flag = not flag
        #     if flag:
        #         #下一轮循环
        #         pass
        #     else:
        #
        #         keep_find('jiyang_jinru')


#委派
def weipai():
    while True:

        point = adb.match('SSL_main')
        if point != None:
            # adb.click(*point)
            break
        else:
            adb.click(*main_juanzhou)       #处理主界面挂机太久需要点返回的情况
            point = adb.match('SSL_main')
            if point != None:
                # adb.click(*point)
                break
            else:
                adb.click(*Btn_Back)
                pass
        sleep(base_delay)
    GetIn.getin_Weipai()
    sleep(base_delay)
    keep_find('Weipai_Flag')
    point = adb.match('Weipai_Mizhu_1')
    if point != None:
        adb.click(*point)
        sleep(base_delay)
        while True:
            point = adb.match('Weipai_Shishen')
            if point != None:
                adb.click(*point)
                sleep(base_delay)
                keep_find('SSL_Quanbu')
                for point in ZB_SSL_Kapian:
                    sleep(base_delay)
                    adb.click(*point)
                sleep(base_delay * 2)
                adb.click(*tiaozhan)
                sleep(base_delay * 2)
                break
            else:
                adb.click(*Btn_Weipai_Skip)
            point = adb.match('Weipai_Zhaohui')
            if point != None:
                adb.click(*Btn_Weipai_Zhaohui)
                break
            else:pass
            point = adb.match('Weipai_Fin')
            if point != None:
                adb.click(*point)
                sleep(base_delay)
                adb.click(*Btn_Back)
                break
            else:
                pass
    else:pass
    sleep(base_delay)
    adb.click(*Btn_Back)
    sleep(base_delay)
    adb.click(*Btn_Back)

#签到
def qiandao():
    sleep(base_delay)
    try:
        point = keep_find('qiandao')
    except:
        return
    adb.click(*point)
    sleep(base_delay * 2)
    adb.click(*qiandao_p)
    sleep(base_delay)
    '''
    find Fin_001
    中间会弹出累计奖励（每五天），等到日子补写
    '''
    point = adb.match('Fin_001')  # 处理挑战卷不足的情况
    if point != None:  # 如果攻打按钮还在，
        adb.click(*point)
    else:
        pass


    keep_find_multiple(['jieqian','jieqian_2'])
    adb.click(*qiandao_exit)

    point = keep_find('qiandao_fudai')
    adb.click(*point)

    point = keep_find('jiangli')
    adb.click(*tansuo)

#邮件
def youjian():
    sleep(base_delay)
    point = keep_find('main_youjian')
    adb.click(*point)
    sleep(base_delay*2)
    point = adb.match('youjian_receive')
    if point != None:
        adb.click(*point)
        point = keep_find('youjian_confirm')
        adb.click(*youjian_receive_confirm)
        point = keep_find('jiangli')
        adb.click(*youjian_receive_confirm)

    else:
        pass
    point = keep_find('youjian_youxiang')
    adb.click(*youjian_back)

#每日一抽
def chouka_daily():
    while True:
        point = adb.match('SSL_main')
        if point != None:
            # adb.click(*point)
            break
        else:
            adb.click(*main_juanzhou)       #处理主界面挂机太久需要点返回的情况
            point = adb.match('SSL_main')
            if point != None:
                # adb.click(*point)
                break
            else:
                adb.click(*Btn_Back)
                pass
        sleep(base_delay)
    adb.click(*Btn_Zhaohuan)
    point = adb.match('Meiri_Chouka')
    if point != None:
        adb.click(*point)
    pass




#真蛇
def true_snake():
    point = keep_find('zhenshe_entry')
    adb.click(*point)
    point = keep_find('zhenshe_tiaozhan')
    adb.click(*point)
    point = keep_find('Confirm_Btn')
    adb.click(*point)
    point = keep_find('zhenshe_chuangjian')
    adb.click(*point)

    '''
    这里写识别倒出真蛇直到战斗完毕内容
    :return:
    '''
    #战斗结束出蛇框
    point = adb.match('snake_sword')
    if point != None:
        adb.click(*snake_confirm)
    else:
        pass
    point = keep_find('Fin_001')
    adb.click(*point)

#魂王
def hun12():
    while True:
        adb.click(*tiaozhan)
        sleep(2)
    pass

def dally():
    digui()

#地鬼
def digui():
    Digui_Choice =  int(r.get('Digui_Switch'))
    if Digui_Choice == 0 :return
    t = time.localtime()
    if t.tm_hour < 10:
        print('为确保地鬼功能正常运作，请等待十点之后再执行命令')
        return
    adb.click(*tansuo)
    point = keep_find('tansuo_digui')
    adb.click(*point)
    point = keep_find('Digui_SSL')
    adb.click(*point)

    base.SSL_switch(0,2)
    sleep(base_delay)

    #到达地域鬼王主界面
    for i in range(Digui_Choice):
        # adb.click(*Digui_Shaixuan)
        point = keep_find('Digui_shaixuan')
        adb.click(*point)
        sleep(base_delay)
        adb.click(*Digui_Remen)
        keep_find('Digui_JSS')
        if i == 0:
            point = digui1
        elif i == 1:
            point = digui2
        elif i == 2:
            point = digui3
        adb.click(*point)
        point = keep_find('Digui_tiaozhan')
        adb.click(*point)
        keep_find('Fight_Ready')
        adb.click(*tiaozhan)
        sleep(10)
        point = keep_find_slow('Fin_002')
        adb.click(*point)
        point = keep_find('Fin_001')
        adb.click(*point)
        keep_find('Digui_tiaozhan')
        adb.click(*Digui_Back)
    #战斗结束，返回主界面
    point = keep_find('Digui_SSL')
    adb.click(*Btn_Back)
    point = keep_find('tansuo_digui')
    adb.click(*Btn_Back)


#魂水
def hunshui(time,need = 30):
    # global x1, x2, y1, y2
    # startpoint = (x1 + 1300, y1 + 700)
    now = 0
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
        point = keep_find('Fin_HunShui')
        adb.click(*tiaozhan)
        point = keep_find('Fin_001')
        adb.click(*point)
        # sleep(5)
        # adb.click(x,y)
        if now == need:
            break
        sleep(7)

    if debug:print('战斗结束')

#斗技
