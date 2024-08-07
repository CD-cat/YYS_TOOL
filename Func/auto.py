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

        # region 异常处理
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
        # endregion

        data = r.get('log_fight').decode('utf-8')
        fight_log = json.loads(data)
        today = time.strftime('%Y-%m-%d', time.localtime())
        if fight_log['date'] != today:base.clear_log()

        with open("./data/game_data/log_time.txt", "r") as f:  # 打开文件
            data = f.read()  # 读取文件
            global time_log
            time_log = json.loads(data)

        # data = r.get('Task_List').decode('utf-8')
        # Task_list = json.loads(data)
        Time_list = time.localtime()

        if Running_Flag == False:
            # Running_Flag = True

            time1 = datetime.datetime.now()
            now_time = time1.strftime('%Y-%m-%d %H:%M:%S')

            jiyang_time = datetime.datetime.strptime(r.get('Jiyang_Flag').decode('utf-8'), "%Y-%m-%d %H:%M:%S")
            time_cha = (time1 - jiyang_time).total_seconds()
            if (time_cha) >3600*6:
                print('执行寄养')
                Running_Flag = True
                r.set('Speed_Flag',0)
                jiyang_flag,taigu_flag = richang.jiyang()
                if jiyang_flag == 1:
                    r.set('Jiyang_Flag',now_time)
                    r.set('Speed_Flag', 1)
                    # r.lset('Taigu_Count',taigu_flag,int(r.lindex('Taigu_Count',taigu_flag))+1)
                    r.hset('Taigu_Sum', taigu_flag,int(r.hget('Taigu_Sum',taigu_flag))+1)
                    r.lpush('Jiyang_Log', now_time+' 寄养' +str(taigu_flag)+ '星太鼓')
                elif jiyang_flag == 3:
                    now_time = (jiyang_time + datetime.timedelta(minutes= 2)).strftime('%Y-%m-%d %H:%M:%S')
                    r.set('Jiyang_Flag', now_time)
                    # r.set('Speed_Flag', 1)



        if Running_Flag == False and int(r.get('daily')) == 0:
            sleep(richang.base_delay)
            Running_Flag = True
            print('执行签到')
            sleep(richang.base_delay)
            richang.qiandao()
            sleep(richang.base_delay)
            richang.youjian()
            sleep(richang.base_delay)
            r.set('daily', 1)


        if Time_list.tm_hour%2==0 and int(r.hget('Task_Queue','weipai'))==1 and Running_Flag == False:
            Running_Flag = True
            print('执行委派')

            richang.weipai()
            r.hset('Task_Queue', 'weipai', 0)
        elif Time_list.tm_hour%2==1 and int(r.hget('Task_Queue','weipai')) == 0 :
            r.hset('Task_Queue','weipai',1)

        elif int(r.hget('Task_Queue','jiejie'))==1 and Running_Flag == False:
            print('执行结界')
            Running_Flag = True
            r.hset('Task_Queue','jiejie',0)
            jiejie.jiejie()

        elif int(r.hget('Task_Queue','digui'))==1 and Time_list.tm_hour >=10 and Running_Flag == False:
            print('执行地鬼')
            Running_Flag = True
            richang.digui()
            r.hset('Task_Queue', 'digui', 0)

        elif int(r.hget('Task_Queue','yuhun'))==1 and Running_Flag == False :
            print('执行御魂')
            Running_Flag = True

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
            r.hset('Task_Queue', 'yuhun', 0)

        elif int(r.hget('Task_Queue','fengmo'))==1 and Time_list.tm_hour>=19 \
                and Time_list.tm_hour<=22 and Running_Flag == False:
            print('执行封魔')
            Running_Flag = True

            FengMo.fengmo()
            r.hset('Task_Queue', 'fengmo', 0)

        elif int(r.hget('Task_Queue','yinjie'))==1 and Time_list.tm_hour>=19 :
            print('执行阴界')
            Running_Flag = True

            richang.yinjie()
            r.hset('Task_Queue', 'yinjie', 0)

        elif int(r.hget('Task_Queue','huahe'))==1 and Time_list.tm_hour>=20 and Running_Flag == False:
            print('领取花合战每日')
            Running_Flag = True

            base.huahezhan()
            r.hset('Task_Queue', 'huahe', 0)

        elif int(r.hget('Task_Queue','liaojinbi'))==1 and Running_Flag == False :
            print('领取每日寮金币')
            Running_Flag = True

            richang.liao_jinbi()
            r.hset('Task_Queue', 'liaojinbi', 0)



        # Task_List_Str = json.dumps(Task_list)
        # r.set('Task_List',Task_List_Str)
        # with open("./data/game_data/Task_List.txt", "w") as f:  # 打开文件
        #     f.write(Task_List_Str)
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
        error_str ='异常记录：'+str(time.asctime())+'\n'+ traceback.format_exc()
        error_flag += 1
        r.set('ERROR_FLAG',error_flag)
        r.lpush('ERROR_LOG',error_str)
        with open("./data/game_data/Error_Log.txt", "a") as f:  # 打开文件
            f.writelines('异常记录：'+time.asctime())
            f.writelines('\n___________________________________________________\n')
            f.write(traceback.format_exc())
            f.writelines('___________________________________________________\n\n')


