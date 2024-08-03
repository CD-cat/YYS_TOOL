import json
from PyQt5.QtWidgets import QMessageBox
DEBUG = True

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