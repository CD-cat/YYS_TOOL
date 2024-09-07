import sys,time
from PyQt5.QtWidgets import QMainWindow, QApplication,QDialog
from PyQt5.QtWidgets import QMessageBox
import random,datetime

# import Func.jiejie
import Func.FengMo
import Func.douji
import Func.yuhun
# import Func.auto
from Func import richang
from Func import base,jiejie,FengMo,exception,HuiJuan,init_redis
from UI.YYS import *
from UI.yuhun_Choice import *
from UI.graph import *
from UI.Setting import *
# from Firm import *
# from Thread.therad import New_Thread
import sys
from time import sleep, ctime
from adb import save_sc
import adb
#终止线程
import ctypes
import inspect
import threading


from Func.untitled import  openMobil,Self_check
from Func.huodong import zhounian
from Func.base import save_img,start_yys,cv_test,keep_find_multiple_slow
from Func.richang import dally,hun12
from Func.yuhun import hun_fight
from Func import richang,untitled,auto
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtChart import QBarSet, QBarSeries, QChart, QChartView, QValueAxis, QBarCategoryAxis, \
    QBarLegendMarker, QVBarModelMapper, QHBarModelMapper, QHorizontalBarSeries, QPercentBarSeries, \
    QHorizontalPercentBarSeries, QHorizontalStackedBarSeries, QStackedBarSeries

#测试用
from Func import GetIn
#

from threading import Thread
import json,redis

DEBUG = True
# DEBUG = False

r = base.r
class Thread1(QThread):
    signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.running = False

    def get_id(self):

        # returns id of the respective thread
        if hasattr(self, '_thread_id'):
            return self._thread_id
        for id, thread in threading._active.items():
            if thread is self:
                return id

    def run(self):
        self.running = True
        count = 0
        # while self.running and count < 17:
        #     print('线程执行中'+str(count))
        #     self.signal.emit(str(count))
        #     Func.yuhun.hun_fight(15, 1)
        #     count += 1
        #     sleep(1)

        while self.running:
            self.signal.emit(str('线程执行中' + str(count)))
            auto.Auto_Run()
            count +=1
            speed_flag = int(r.get('Speed_Flag'))
            if speed_flag:
                sleep(60)
            else:
                sleep(15)
            if count >10000:count =0


    def raise_exception(self):
        thread_id = self.get_id()
        res = ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id,
            ctypes.py_object(SystemExit))
        if res > 1:
            ctypes.pythonapi.PyThreadState_SetAsyncExc(thread_id, 0)
            print('Exception raise failure')
        print('终止线程测试')

    def stop(self):
        self.running = False

        self.wait()

# def stop_thread(thread):
#     _async_raise(thread.ident, SystemExit)


class Thread2(QThread):
    signal = pyqtSignal(str)

    def __init__(self):
        super().__init__()
        self.running = False

    def run(self):
        self.running = True
        count = 0
        while self.running:
            with open("./data/game_data/huodong_data.txt", "r") as f:  # 打开文件
                data = f.read()  # 读取文件
                print(data)
            huodong_dict = json.loads(data)
            num1 = huodong_dict['time']
            num2 = huodong_dict['count']
            zhounian(num1,num2)
            count += 1
            sleep(1)



    def stop(self):
        self.running = False



class MainWindow(QMainWindow, Ui_MainWindow):


    def __init__(self, parent=None):
        with open("./data/game_data/huodong_data.txt", "r") as f:  # 打开文件
            data = f.read()  # 读取文件
            print(data)
        huodong_dict = json.loads(data)

        super(MainWindow, self).__init__(parent)

        self.thread1 = Thread1()
        self.thread2 = Thread2()

        base.clear_log()

        self.setupUi(self)
        self.lineEdit_7.setText(str(huodong_dict['time']))
        self.lineEdit_8.setText(str(huodong_dict['count']))
        self.pushButton.clicked.connect(self.btn_click_1)

        self.pushButton_3.clicked.connect(self.btn_click_3)#YYS启动

        self.pushButton_6.clicked.connect(self.btn_click_6)#自检
        self.pushButton_7.clicked.connect(self.btn_click_7)#御魂
        self.pushButton_8.clicked.connect(self.btn_click_8)#活动
        self.pushButton_9.clicked.connect(self.btn_click_9)#魂王
        self.pushButton_10.clicked.connect(self.thread1_stop)  # 日常线程终止
        self.pushButton_11.clicked.connect(self.thread2_stop)  # 线程终止
        self.pushButton_12.clicked.connect(self.btn_click_12)  # 关闭模拟器



        # self.pushButton_14.clicked.connect(self.btn_click_14)  # 线程启动
        self.pushButton_14.clicked.connect(self.thread1_start)  # 线程启动

        self.pushButton_15.clicked.connect(self.btn_click_15)  # 地鬼

        self.pushButton_18.clicked.connect(self.btn_click_18)  # 持续点击
        # self.pushButton_19.clicked.connect(child.show)  # 持续点击
        self.pushButton_21.clicked.connect(self.btn_click_21)  # 结界突破
        self.pushButton_22.clicked.connect(self.btn_click_22)  # 委派
        self.pushButton_23.clicked.connect(self.btn_click_23)  # 斗技
        self.pushButton_25.clicked.connect(self.btn_click_25)  # 链接模拟器

    #按钮链接
    def btn_click_13(self):#功能测试
        if DEBUG: print('Btn13 Click')
        if DEBUG: print('功能测试')
        # FengMo.find_lanpiao()
        # richang.digui()
        # richang.weipai()
        # adb.swipe(1744,215,1744,825,210)
        # richang.fengmo()
        # richang.true_snake()
        # richang.qiandao()
        # richang.youjian()
        # jiejie.jiejie_fight(3)
        # untitled.test()
        # richang.hun11(18,1)
        # richang.find_lanpiao()
        # base.SSL_Deal_tuozhan()
        # adb.swipe(800, 2000, 1744, 2000, 210)
        # GetIn.getin_yuhun('shui')
        # keep_find_multiple_slow('douji_fenxiang')
        #
        # for i in range(20):
        #     Func.douji.douji()
        # base.huahezhan()
        # base.clear_log()
        # richang.youjian()
        # richang.liao_jinbi()
        # richang.test()
        # exception.deal_exception()
        # exception.restart()
        # richang.jiyang()
        # richang.yinjie()
        # adb.swipe(560, 825, 560, 715, 12)
        # adb.click(560, 825)
        # flag = True
        # point = adb.match('jiejieka_taigu_6', 0.98)  # 六星太古
        # if point != None:
        #     flag = not flag
        # if flag:
        #     point = adb.match('jiejieka_taigu_5', 0.98)  # 五星太鼓
        #     if point != None:
        #         flag = not flag
        # if flag:
        #     point = adb.match('jiejieka_taigu_4', 0.98)  # 四星太古
        #     if point != None:
        #         flag = not flag
        # taigu_flag = 6
        # now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # r.hset('Taigu_Sum', taigu_flag, int(r.hget('Taigu_Sum', taigu_flag)) + 1)
        # r.lpush('Taigu_Log', now_time+' 寄养' +str(taigu_flag)+ '星太鼓')
        # point = adb.match('YYS_WY')
        # adb.click(*point)
        # untitled.open_YYS()
        # exception.restart()
        # HuiJuan.Kun28()
        # HuiJuan.Huijuan_Auto()
        # point = base.keep_find('jiejie_refresh')
        # adb.click(*point)
        # point = base.keep_find('jiejie_refresh_confirm')
        # adb.click(*point)
        # jiejie.jiejie_fight()
        # richang.shop_daily()
        jiejie.jiejie()



    def thread1_start(self):
        # self.thread1.signal.connect(self.update_thread1_display)
        self.thread1.signal.connect(self.update_thread1_display)
        self.thread1.start()

    def thread1_stop(self):
        self.thread1.signal.disconnect()
        # self.thread1.raise_exception()
        self.thread1.stop()
        # stop_thread(self.thread1)

    def thread2_stop(self):
        self.thread2.signal.disconnect()
        self.thread2.stop()


    def update_thread1_display(self, text):
        # self.thread1_display_label.setText(text)
        self.lineEdit_5.setText(text)

    def btn_click_1(self):
        if DEBUG : print('Btn1 Click')
        openMobil()

    def btn_click_2(self):
        if DEBUG : print('Btn2 Click')
        pic_name = self.lineEdit_2.text()
        save_img(pic_name)
        self.lineEdit_2.clear()

    def btn_click_3(self):
        if DEBUG : print('Btn3 Click')
        # start_yys()
        untitled.open_YYS()

    def btn_click_4(self):
        if DEBUG : print('Btn4 Click')
        x_v = self.lineEdit_3.text()
        y_v = self.lineEdit_4.text()
        adb.click(x_v, y_v)
        # adb.click(150, 1960)

    def btn_click_5(self):
        if DEBUG : print('Btn5 Click')
        name = self.lineEdit_10.text()
        cv_test(name)

    def btn_click_6(self):
        # Self_check()
        untitled.check_once()

        if DEBUG : print('Btn6 Click')
    #御魂
    def btn_click_7(self):#御魂
        if DEBUG: print(time_log['shui'])
        with open("./data/game_data/yuhun.txt", "r") as f:  # 打开文件
            data = f.read()  # 读取文件
            print(data)
        yuhun_choice = json.loads(data)
        yuhun_index = ['tu', 'wang', 'shui', 'huo', 'ri', 'shi']
        if DEBUG : print('Btn7 Click')
        Func.yuhun.yuhun(yuhun_index[yuhun_choice[int(fight_log['weekday'])]])
        if yuhun_choice[7]:
            sleep(richang.base_delay*3)
            jiejie.jiejie()

    def btn_click_8(self):
        err_flag = True #为真则正常调用方法，为假说明有异常
        if DEBUG : print('Btn8 Click')
        num1 = self.lineEdit_7.text()
        num2 = self.lineEdit_8.text()
        if num2 :
            try:
                num1 = int(num1)
                num2 = int(num2)

            except:
                msg_box = QMessageBox(QMessageBox.Critical, '错误', '通关时间和次数仅能输入数字')
                msg_box.exec_()
                err_flag = False
        else:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '请输入通关时间')
            msg_box.exec_()
            err_flag = False
        if  err_flag :
            huodong_dict = json.loads('{"time": 0, "count": 0}')
            huodong_dict['time'] = num1
            huodong_dict['count'] = num2
            huodong_str = json.dumps(huodong_dict)
            with open("./data/game_data/huodong_data.txt", "w") as f:  # 打开文件
                f.write(huodong_str)

            # zhounian(time=num1, need=num2)
            self.thread2.run()
            # richang.hun11(time=num1, need=num2)

    def btn_click_9(self):
        err_flag = True #为真则正常调用方法，为假说明有异常
        hun12()

    def btn_click_12(self):
        untitled.end_program('Nox.exe')

        # untitled.check_once()

        if DEBUG : print('Btn12 关闭模拟器')

    # 地鬼
    def btn_click_15(self):#地鬼
        if DEBUG : print('Btn15 地鬼任务开始')
        richang.digui()

    def btn_click_16(self):
        if DEBUG : print('Btn16 Click')
        dally()

    def btn_click_17(self):
        if DEBUG : print('Btn17 Click')
        x_v = int(self.lineEdit_3.text())
        y_v = int(self.lineEdit_4.text())
        while  True:
            adb.click(x_v + random.randint(1,15) * random.choice([1,-1]) , y_v+ random.randint(1,15) * random.choice([1,-1]))
            sleep(5.33 + round(random.random(),2) * random.choice([1,-1]))
        # adb.click(150, 1960)

    def btn_click_18(self):
        if DEBUG : print('Btn18 Click 逢魔')
        Func.FengMo.fengmo()
        # dally()

    def btn_click_19(self):
        if DEBUG : print('Btn19 Click 呼出子窗口')
        # self.chile_Win = Child()
        self.child.show()
        # self.child.exec_()
        # child_window = Child()
        # child_window.show()

    def btn_click_20(self):
        if DEBUG : print('Btn20 Click 呼出子窗口2')
        # self.chile_Win = Child()
        self.child.show()
        # self.child.exec_()
        # child_window = Child()
        # child_window.show()

    def btn_click_21(self):
        if DEBUG : print('Btn21 Click 结界突破')
        jiejie.jiejie()

    def btn_click_22(self):
        if DEBUG : print('Btn22 Click 式神委派')
        richang.weipai()

    def btn_click_23(self):
        if DEBUG : print('Btn23 Click 斗技')
        count = int(self.lineEdit_15.text())
        for i in range(count):
            Func.douji.douji()

    def btn_click_25(self):
        if DEBUG : print('Btn25 Click 连接模拟器')
        adb.connect()



class ChildWindow(QDialog, Ui_Dialog1):
    def __init__(self):
        super(ChildWindow, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_click_1)
        self.pushButton_2.clicked.connect(self.btn_click_2)


        with open("./data/game_data/yuhun.txt", "r") as f:  # 打开文件
            data = f.read()  # 读取文件
            print(data)
        yuhun_list = json.loads(data)


        self.comboBox.setCurrentIndex(yuhun_list[1])
        self.comboBox_2.setCurrentIndex(yuhun_list[2])
        self.comboBox_3.setCurrentIndex(yuhun_list[3])
        self.comboBox_4.setCurrentIndex(yuhun_list[4])
        self.comboBox_5.setCurrentIndex(yuhun_list[5])
        self.comboBox_6.setCurrentIndex(yuhun_list[6])
        self.comboBox_7.setCurrentIndex(yuhun_list[0])
        self.comboBox_8.setCurrentIndex(yuhun_list[7])

        # region 御魂战斗时间
        with open("./data/game_data/log_time.txt", "r") as f:  # 打开文件
            data = f.read()  # 读取文件
            print(data)
        yuhun_time = json.loads(data)
        self.lineEdit.setText(str(yuhun_time['tu']))
        self.lineEdit_2.setText(str(yuhun_time['wang']))
        self.lineEdit_3.setText(str(yuhun_time['shui']))
        self.lineEdit_4.setText(str(yuhun_time['huo']))
        self.lineEdit_5.setText(str(yuhun_time['ri']))
        self.lineEdit_6.setText(str(yuhun_time['shi']))
        # endregion

        # region 每日御魂次数
        with open("./data/game_data/yuhun_time.txt", "r") as f:  # 打开文件
            data = f.read()  # 读取文件
            print(data)
        yuhun_count = json.loads(data)
        self.lineEdit_8.setText(str(yuhun_count[1]))
        self.lineEdit_9.setText(str(yuhun_count[2]))
        self.lineEdit_10.setText(str(yuhun_count[3]))
        self.lineEdit_11.setText(str(yuhun_count[4]))
        self.lineEdit_12.setText(str(yuhun_count[5]))
        self.lineEdit_13.setText(str(yuhun_count[6]))
        self.lineEdit_14.setText(str(yuhun_count[0]))
        # endregion

    def btn_click_1(self):
        if DEBUG: print('Btn1 Click 子窗体1')
        err_flag = True  # 为真则正常调用方法，为假说明有异常

        t_tu = self.lineEdit.text()
        t_wang = self.lineEdit_2.text()
        t_shui = self.lineEdit_3.text()
        t_huo = self.lineEdit_4.text()
        t_ri = self.lineEdit_5.text()
        t_shi = self.lineEdit_6.text()

        count1 = self.lineEdit_8.text()
        count2 = self.lineEdit_9.text()
        count3 = self.lineEdit_10.text()
        count4 = self.lineEdit_11.text()
        count5 = self.lineEdit_12.text()
        count6 = self.lineEdit_13.text()
        count7 = self.lineEdit_14.text()
        if t_tu and t_wang and t_shui and t_huo and t_ri and count1 and count2 and count3 and count4 and count5 and count6 and count7:
            try:
                t_tu = int(t_tu)
                t_wang = int(t_wang)
                t_shui = int(t_shui)
                t_huo = int(t_huo)
                t_ri = int(t_ri)
                t_shi = int(t_shi)

                count1 = int(count1)
                count2 = int(count2)
                count3 = int(count3)
                count4 = int(count4)
                count5 = int(count5)
                count6 = int(count6)
                count7 = int(count7)

            except:
                msg_box = QMessageBox(QMessageBox.Critical, '错误', '战斗时间和次数仅能输入数字')
                msg_box.exec_()
                err_flag = False
        else:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '战斗时间和次数不能为空或0')
            msg_box.exec_()
            err_flag = False
        if err_flag:
            with open("./data/game_data/log_time.txt", "r") as f:  # 打开文件
                data = f.read()  # 读取文件
                print(data)
            yuhun_time = json.loads(data)
            yuhun_time['tu'] = t_tu
            yuhun_time['wang'] = t_wang
            yuhun_time['shui'] = t_shui
            yuhun_time['huo'] = t_huo
            yuhun_time['ri'] = t_ri
            yuhun_time['shi'] = t_shi
            huodong_str = json.dumps(yuhun_time)
            with open("./data/game_data/log_time.txt", "w") as f:  # 打开文件
                f.write(huodong_str)

            with open("./data/game_data/yuhun_time.txt", "r") as f:  # 打开文件
                data = f.read()  # 读取文件
                print(data)
            yuhun_count = json.loads(data)
            yuhun_count[1] = count1
            yuhun_count[2] = count2
            yuhun_count[3] = count3
            yuhun_count[4] = count4
            yuhun_count[5] = count5
            yuhun_count[6] = count6
            yuhun_count[0] = count7

            huodong_str = json.dumps(yuhun_count)
            with open("./data/game_data/yuhun_time.txt", "w") as f:  # 打开文件
                f.write(huodong_str)

        with open("./data/game_data/yuhun.txt", "r") as f:  # 打开文件
            data = f.read()  # 读取文件
            if DEBUG: print(data)
        yuhun_list = json.loads(data)
        yuhun_list[1] = self.comboBox.currentIndex()
        yuhun_list[2] = self.comboBox_2.currentIndex()
        yuhun_list[3] = self.comboBox_3.currentIndex()
        yuhun_list[4] = self.comboBox_4.currentIndex()
        yuhun_list[5] = self.comboBox_5.currentIndex()
        yuhun_list[6] = self.comboBox_6.currentIndex()
        yuhun_list[0] = self.comboBox_7.currentIndex()
        yuhun_list[7] = self.comboBox_8.currentIndex()

        fight_log_str = json.dumps(yuhun_list)
        with open("./data/game_data/yuhun.txt", "w") as f:  # 打开文件
            f.write(fight_log_str)
        self.close()

    def btn_click_2(self):
        if DEBUG: print('Btn2 Click 子窗体1')
        self.close()




    #     # 绑定按钮点击事件
    #     self.Button_Start.clicked.connect(self.Start)
    #     self.Button_Stop.clicked.connect(self.Stop)
    #
    # def Stop(self):
    #     print('End')
    #     self.thread.terminate()  # 终止线程
    #
    # def Start(self):
    #     print('Start clicked.')
    #     self.thread = New_Thread(t=100)  # 实例化一个线程，参数t设置为100
    #     # 将线程thread的信号finishSignal和UI主线程中的槽函数Change进行连接
    #     self.thread.finishSignal.connect(self.Change)
    #     # 启动线程，执行线程类中run函数
    #     self.thread.start()
    #
    # # 接受通过emit传来的信息，执行相应操作
    # def Change(self, msg):
    #     print(msg)
    #     self.label.setText(str(msg))


class ChildWindow_Setting(QDialog, Ui_Dialog_Setting):
    def __init__(self):
        super(ChildWindow_Setting, self).__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.btn_click_1)
        self.pushButton_2.clicked.connect(self.btn_click_2)

        self.comboBox.setCurrentIndex(int(r.get('Server_Switch')))
        self.comboBox_2.setCurrentIndex(int(r.get('Digui_Switch')))
        self.comboBox_3.setCurrentIndex(int(r.hget('Task_Flag', 'fengmo')))
        self.comboBox_4.setCurrentIndex(int(r.hget('Task_Flag', 'fudai')))
        self.comboBox_5.setCurrentIndex(int(r.hget('Task_Flag', 'yinjie')))
        self.comboBox_6.setCurrentIndex(int(r.hget('Task_Flag', 'jiejie')))
        self.comboBox_7.setCurrentIndex(int(r.get('Simulator_Switch')))
        self.comboBox_8.setCurrentIndex(int(r.hget('Task_Flag', 'fengmo')))
        self.comboBox_9.setCurrentIndex(int(r.hget('Huodong', 'flag')))
        self.lineEdit.setText(r.get('base_delay').decode('utf-8'))
        self.lineEdit_2.setText(r.hget('Huodong', 'time').decode('utf-8'))
        self.lineEdit_3.setText(r.hget('Huodong', 'number').decode('utf-8'))

    def btn_click_1(self):
        err_flag = True  # 为真则正常调用方法，为假说明有异常

        if DEBUG: print('Btn1 Click 设置窗体')
        Server_Choice = self.comboBox.currentIndex()
        r.set('Server_Switch', Server_Choice)

        Digui_Choice = self.comboBox_2.currentIndex()
        if Digui_Choice == '0': r.hset('Task_Queue', 'digui', 0)
        r.set('Digui_Switch', Digui_Choice)

        Fengmo_Flag = self.comboBox_3.currentIndex()
        # r.hset('Task_Queue', 'fengmo', 1)
        r.hset('Task_Flag', 'fengmo', Fengmo_Flag)

        Fudai_Flag = self.comboBox_4.currentIndex()
        r.hset('Task_Flag', 'fudai', Fudai_Flag)

        yinjie_Flag = self.comboBox_5.currentIndex()
        # r.hset('Task_Queue', 'yinjie', 0)
        r.hset('Task_Flag', 'yinjie', yinjie_Flag)

        jiejie_Flag = self.comboBox_6.currentIndex()
        # r.hset('Task_Queue', 'yinjie', 0)
        r.hset('Task_Flag', 'jiejie', jiejie_Flag)

        Moniqi_Flag = self.comboBox_7.currentIndex()
        # r.hset('Task_Queue', 'yinjie', 0)
        r.set('Simulator_Switch', Moniqi_Flag)

        fengmo_Flag = self.comboBox_8.currentIndex()
        # r.hset('Task_Queue', 'yinjie', 0)
        r.hset('Task_Flag', 'fengmo', fengmo_Flag)

        huodong_Flag = self.comboBox_9.currentIndex()
        # r.hset('Task_Queue', 'yinjie', 0)
        r.hset('Huodong', 'flag', huodong_Flag)

        base_delay = self.lineEdit.text()
        huodong_time = self.lineEdit_2.text()
        huodong_number = self.lineEdit_3.text()

        if base_delay and huodong_time and huodong_number:
            try:
                base_delay = float(base_delay)
                huodong_time = int(huodong_time)
                huodong_number = int(huodong_number)

            except:
                msg_box = QMessageBox(QMessageBox.Critical, '错误', '基础延时仅能输入数字、战斗时间和次数仅能输入整数')
                msg_box.exec_()
                err_flag = False
        else:
            msg_box = QMessageBox(QMessageBox.Critical, '错误', '基础延时、战斗时间和次数不能为空或0')
            msg_box.exec_()
            err_flag = False

        if err_flag:
            if huodong_number != int(r.hget('Huodong', 'number')):
                r.hset('Huodong', 'finish', 0)
            r.set('base_delay', base_delay)
            r.hset('Huodong', 'time', huodong_time)
            r.hset('Huodong', 'number', huodong_number)
            self.close()

    def btn_click_2(self):
        if DEBUG: print('Btn2 Click 设置窗体')
        self.close()








class ChildWindow1(QDialog, Ui_Dialog_Graph):
    # def __init__(self):
    #     super(ChildWindow1, self).__init__()
    #     self.setupUi(self)
    #     self.graphicsView.setBackgroundRole()
    #
    # def btn_click_1(self):
    #     if DEBUG : print('Btn1 Click 子窗体2')
    #
    # def btn_click_2(self):
    #     if DEBUG : print('Btn2 Click 子窗体1')
    #     self.close()

    def __init__(self, parent=None):
        super(ChildWindow1, self).__init__(parent)

        date = []
        c_win = []
        c_lose = []
        count = 1
        with open("./data/game_data/log_fight.txt", "r") as f:  # 读取当天记录
            data = f.readline()  # 读取文件
            message = json.loads(data)
            if message['douji'] != [0, 0]:
                count += 1
                date.append(message['date'][-5:])
                c_win.append(message['douji'][0])
                c_lose.append(message['douji'][1])


        with open("./data/game_data/log_fight_his.txt", "r") as f:  # 打开文件

            while count <=3:
                data = f.readline()  # 读取文件
                message = json.loads(data)
                if message['douji'] != [0,0]:
                    count += 1
                    # print(message['date'])
                    # ddd = message['date'][-5:]
                    # print(ddd)
                    # date.append(ddd)
                    date.append(message['date'][-5:])
                    c_win.append(message['douji'][0])
                    c_lose.append(message['douji'][1])
        date.reverse()
        c_win.reverse()
        c_lose.reverse()
        # c_win +=c_lose
        print(date)
        print(c_win)
        print(c_lose)



        chart = QChart()
        barSeries = QBarSeries()  # 竖向柱状图
        # barSeries = QPercentBarSeries()   # 竖向百分比柱状图
        # barSeries = QHorizontalBarSeries()    # 横向柱状图
        # barSeries = QHorizontalPercentBarSeries()   # 横向百分比柱状图
        # barSeries = QStackedBarSeries() # 竖向堆叠柱状图
        # barSeries = QHorizontalStackedBarSeries() # 横向堆叠柱状图

        chartView = QChartView()
        valueAxisY = QValueAxis()
        barCategorAxisX = QBarCategoryAxis()

        chart.setAnimationOptions(QChart.AllAnimations)
        chart.setAnimationEasingCurve(QEasingCurve.OutBack)

        set0 = QBarSet("胜场")
        set1 = QBarSet("败场")
        set2 = QBarSet("胜率")


        for i in range(len(c_lose)):
            set0.append(int(c_win[i]))
            set1.append(int(c_lose[i]))
            set2.append(c_win[i]/(c_win[i]+c_lose[i])*10)


        # set0.append(10.12345)
        # set0.append(3.23)
        # set0.append(7)
        # set0.append(7)
        #
        # set1.append(5)
        # set1.append(2)
        # set1.append(9)
        #
        # set2.append(9)
        # set2.append(1)
        # set2.append(7)

        barSeries.append(set0)
        barSeries.append(set1)
        barSeries.append(set2)
        barSeries.setBarWidth(0.8)

        barSeries.setLabelsVisible(True)
        barSeries.setLabelsAngle(75.0)
        barSeries.setLabelsPrecision(3)
        # barSeries.setLabelsFormat("")

        barCategorAxisX.append(date)

        valueAxisY.setRange(0, max(c_win+c_lose))

        chart.setTitle("最近三次斗技数据统计")
        chart.setAxisX(barCategorAxisX)
        chart.setAxisY(valueAxisY)
        chart.addSeries(barSeries)

        chartView.setChart(chart)

        vbox = QVBoxLayout()
        vbox.addWidget(chartView)
        self.setLayout(vbox)





    #     self.setWindowTitle(_translate("MainWindow", "摆烂小助手"))





    #     # 绑定按钮点击事件
    #     self.Button_Start.clicked.connect(self.Start)
    #     self.Button_Stop.clicked.connect(self.Stop)
    #
    # def Stop(self):
    #     print('End')
    #     self.thread.terminate()  # 终止线程
    #
    # def Start(self):
    #     print('Start clicked.')
    #     self.thread = New_Thread(t=100)  # 实例化一个线程，参数t设置为100
    #     # 将线程thread的信号finishSignal和UI主线程中的槽函数Change进行连接
    #     self.thread.finishSignal.connect(self.Change)
    #     # 启动线程，执行线程类中run函数
    #     self.thread.start()
    #
    # # 接受通过emit传来的信息，执行相应操作
    # def Change(self, msg):
    #     print(msg)
    #     self.label.setText(str(msg))

if __name__ == '__main__':
    init_redis.Check_Redis()
    with open("./data/game_data/log_time.txt", "r") as f:  # 打开文件
        data = f.read()  # 读取文件
        global time_log
        time_log = json.loads(data)

    with open("./data/game_data/log_fight.txt", "r") as f:  # 打开文件
        data = f.read()  # 读取文件
        print(data)
    fight_log = json.loads(data)

    print(time_log)



    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    # child = QDialog()
    # child_ui = Ui_Dialog1()
    # child_ui.setupUi(child)
    child = ChildWindow()
    child1 = ChildWindow1()
    child_Setting = ChildWindow_Setting()

    btn = main_window.pushButton_19  # 主窗体按钮事件绑定
    btn.clicked.connect(child.show)
    btn = main_window.pushButton_20  # 主窗体按钮事件绑定
    btn.clicked.connect(child1.show)

    btn = main_window.pushButton_24  # 主窗体按钮事件绑定
    btn.clicked.connect(child_Setting.show)


    sys.exit(app.exec())

