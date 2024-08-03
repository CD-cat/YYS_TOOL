import json,time,traceback,redis,datetime
# import Func.FengMo
import Func.douji
import Func.yuhun
from Func import richang,untitled,jiejie,yuhun,base,FengMo,exception
from time import sleep
DEBUG = True
# DEBUG = False

def Auto_Run():
    try:
        #region 异常测试，抛出异常
        # raise Exception('发生异常错误信息')
        #endregion
        #执行标志，每次循环都只执行一个任务
        Running_Flag = False

        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        error_flag = int(r.get('ERROR_FLAG'))
        if error_flag == 0 :pass
        elif error_flag ==1:
            Running_Flag = True
            exception.deal_exception()
            r.set('ERROR_FLAG',0)
        elif error_flag ==2:
            exception.restart()
            Running_Flag = True
            r.set('ERROR_FLAG',0)
        elif error_flag == 3:
            Running_Flag = True
            print('什么寄吧情况')

        data = r.get('log_fight').decode('utf-8')
        fight_log = json.loads(data)
        today = time.strftime('%Y-%m-%d', time.localtime())
        if fight_log['date'] != today:base.clear_log()

        with open("./data/game_data/log_time.txt", "r") as f:  # 打开文件
            data = f.read()  # 读取文件
            global time_log
            time_log = json.loads(data)

        data = r.get('Task_List').decode('utf-8')
        Task_list = json.loads(data)
        Time_list = time.localtime()

        if Running_Flag == False:
            # Running_Flag = True

            time1 = datetime.datetime.now()
            now_time = time1.strftime('%Y-%m-%d %H:%M:%S')

            jiyang_time = datetime.datetime.strptime(r.get('Jiyang_Flag').decode('utf-8'), "%Y-%m-%d %H:%M:%S")
            time_cha = (time1 - jiyang_time).seconds
            if (time_cha) >3600*6:
                Running_Flag = True
                r.set('Speed_Flag',0)
                jiyang_flag = richang.jiyang()
                if jiyang_flag == 1:
                    r.set('Jiyang_Flag',now_time)
                    r.set('Speed_Flag', 1)




        if Time_list.tm_hour%2==0 and Task_list['weipai'][1]==1 and Running_Flag == False:
            Running_Flag = True
            print('执行委派')
            Task_list['weipai'][1] = 0
            richang.weipai()
        elif Time_list.tm_hour%2==1 and Task_list['weipai'][1] == 0 :
            Task_list['weipai'][1] = 1

        elif Task_list['jiejie'][0]==1 and Running_Flag == False:
            print('执行结界')
            Running_Flag = True
            Task_list['jiejie'][0] = 0
            jiejie.jiejie()

        elif Task_list['digui'][0]==1 and Time_list.tm_hour >=10 and Running_Flag == False:
            print('执行地鬼')
            Running_Flag = True
            Task_list['digui'][0] = 0
            richang.digui()

        elif Task_list['yuhun'][0]==1 and Running_Flag == False:
            print('执行御魂')
            Running_Flag = True
            Task_list['yuhun'][0] = 0
            with open("./data/game_data/yuhun.txt", "r") as f:  # 打开文件
                data = f.read()  # 读取文件
                print(data)
            yuhun_choice = json.loads(data)
            yuhun_index = ['tu', 'wang', 'shui', 'huo', 'ri', 'shi']
            if DEBUG: print('Btn7 Click')
            Func.yuhun.yuhun(yuhun_index[yuhun_choice[int(fight_log['weekday'])]])
            if yuhun_choice[7]:
                sleep(richang.base_delay * 3)
                jiejie.jiejie()

        elif Task_list['fengmo'][0]==1 and Time_list.tm_hour>=19 \
                and Time_list.tm_hour<=22 and Running_Flag == False:
            print('执行封魔')
            Running_Flag = True
            Task_list['fengmo'][0] = 0
            FengMo.fengmo()

        elif Task_list['huahe'][0]==1 and Time_list.tm_hour>=22 and Running_Flag == False:
            print('领取花合战每日')
            Running_Flag = True
            Task_list['huahe'][0] = 0
            base.huahezhan()

        elif Task_list['liaojinbi'][0]==1 and Running_Flag == False :
            print('领取每日寮金币')
            Running_Flag = True
            Task_list['liaojinbi'][0] = 0
            richang.liao_jinbi()

        Task_List_Str = json.dumps(Task_list)
        r.set('Task_List',Task_List_Str)
        with open("./data/game_data/Task_List.txt", "w") as f:  # 打开文件
            f.write(Task_List_Str)
        # Huahe_Flag = True
        # for i in Task_list:
        #     if i[0]:
        #         Huahe_Flag = False
        #         break
        # if Huahe_Flag:
        #     base.huahezhan()
    except:
        print('线程异常，请检查')
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        error_flag = int(r.get('ERROR_FLAG'))
        error_flag += 1
        r.set('ERROR_FLAG',error_flag)
        r.lpush('ERROR_LOG',traceback.format_exc())
        with open("./data/game_data/Error_Log.txt", "a") as f:  # 打开文件
            f.writelines('异常记录：'+time.asctime())
            f.writelines('\n___________________________________________________\n')
            f.write(traceback.format_exc())
            f.writelines('___________________________________________________\n\n')


