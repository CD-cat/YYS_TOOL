import os
import subprocess
from time import sleep
from Func.base import *
import adb
from Func.point_zb import *
import os
from Func import richang,base
import json,redis


# 关闭其他应用程序
        # pro_name:将要关闭的程序

r = base.r
base_delay = float(r.get('base_delay').decode('utf-8'))
def end_program(pro_name):
    os.system('%s%s' % ("taskkill /F /IM ", pro_name))

def Self_check():
    while True:

        key = adb.adb('shell wm size')
        if key == bytes():
            break

    # print(adb.device_check())
    pass


def check_once():

    key = adb.adb('shell wm size')
    # adb.device_check()
    if key == bytes():
        print(key)
        # end_program('Nox.exe')
        pass
    else:
        # sleep(20)
        print(key)
        pass

def openMobil():
    # os.popen(r'D:\1.nox\Nox\bin\Nox.exe -clone:Nox_1')
    # os.popen(r'.D:\0.project\5.YYS_Tool\open.bat')
    # open('./open.bat')
    # cmd = 'cmd.exe d:/start.bat'

    directory = 'YYS_YOOL'
    filename = 'open.bat'
    current_path = os.getcwd()
    absolute_path = os.path.join(current_path,  filename)
    print(absolute_path)

    # abs_path = os.path.abspath('../open.bat')
    # print(abs_path)
    p = subprocess.Popen("cmd.exe /c" + absolute_path, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    curline = p.stdout.readline()
    while (curline != b''):
        print(curline)
        curline = p.stdout.readline()
    p.wait()
    print(p.returncode)

    print('555')
    sleep(5)
    while True:
        sleep(1)
        key = adb.adb('shell wm size')
        if key == bytes():
            print('模拟器已启动，虚拟机开机未完成')
            pass
        else:
            sleep(20)
            break
    r.set('ERROR_FLAG', 0)
    open_YYS()

def open_YYS():
    YYS_List = [
        ['YYS_WY','YYS_B','YYS_WY'],    #夜神
        ['YYS_WY_LD','YYS_WY_LD','YYS_WY_LD'],      #雷电
        ['YYS_WY_BS', 'YYS_WY_BS','YYS_WY_BS'],     #蓝叠BlueStacks
        ['YYS_WY', 'YYS_WY','YYS_WY']      #待定
        ]
    point = keep_find(YYS_List[int(r.get('Simulator_Switch'))][int(r.get('Server_Switch'))])
    adb.click(*point)
    sleep(base_delay*12)
    entry_YYS()


def entry_YYS():
    point,picname = keep_find_multiple_slow(['8+','New_Huodong','Sys_Restart'])#多目标检索，差游戏公告
    if picname == 'New_Huodong':
        adb.click(*Btn_exit_Gonggao)
        point = keep_find('8+')
        sleep(base_delay * 15)
        adb.click(*Btn_Start)
    elif picname == 'Sys_Restart':
        adb.click(*point)
    else:
        sleep(base_delay * 15)
        adb.click(*Btn_Start)
    sleep(30)#增加市场
    #处理插画下载弹窗
    point = adb.match('main_chahua')
    if point != None:
        '''
        这里需要加入勾选30天不提示
        '''
        point = keep_find('main_chahua_download')
        adb.click(*point)
    else:
        pass
    sleep(base_delay)
    # with open("./data/game_data/log_fight.txt", "r") as f:  # 打开文件
    #     data = f.read()  # 读取文件
    #     print(data)
    # fight_log = json.loads(data)
    daily_flag = int(r.hget('Task_Queue', 'daily'))
    if daily_flag == 1 :
        richang.qiandao()
        sleep(base_delay)
        richang.youjian()
        sleep(base_delay)
        r.hset('Task_Queue', 'daily', 0)
    # point = adb.match('qiandao')
    # if point != None:
    #     richang.qiandao()
    # else:
    #     pass

def test():
    point = keep_find('main_youjian')
    sleep(3)
    point = adb.match('main_chahua')
    if point != None:
        point = keep_find('main_chahua_download')
        adb.click(*point)
    else:
        pass




    return 1


# def open():
#     os.system(r'D:\1.nox\Nox\bin\Nox.exe -clone:Nox_1')


def close():
    pid = os.getpid()
    if os.name == 'nt':  # Windows系统
        cmd = 'taskkill /pid ' + str(pid) + ' /f'
        try:
            os.system(cmd)
            print(pid, 'killed')
        except Exception as e:
            print(e)
# close()
# open()