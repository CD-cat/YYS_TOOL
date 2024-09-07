import redis,json
from Func import base
with open("./Redis_Info.txt", "r") as f:  # 打开文件
    data = f.read()  # 读取文件
    print(data)
Redis_Info = json.loads(data)

r = redis.StrictRedis(host=Redis_Info[0], port=Redis_Info[1], db=Redis_Info[2])
def Check_Redis():
    try:
        init_flag = False
        key_list = [
            'base_delay',
            'ERROR_FLAG',
            'log_fight',
            'Server_Switch',
            'Digui_Switch',
            'Jiyang_Flag',
            'Speed_Flag',
            'Task_List',
            'Simulator_Switch'
        ]
        hash_key_list = {
            'Task_Flag':[
                'fengmo',
                'yinjie',
                'yuhun',
                'fudai',
                'jiejie',
            ],
            'Task_Queue':[
                'yinjie',
                'weipai',
                'jiejie',
                'digui',
                'yuhun',
                'fengmo',
                'liaojinbi',
                'huahe',
                'daily'
            ],
            'Taigu_Sum':['4','5','6'],
            'Huodong':[
                'flag',
                'time',
                'number',
                'finish'
            ]
        }
        for key in key_list:
            if not r.exists(key):init_flag = True
        for hash in hash_key_list:
            for key in hash_key_list[hash]:
                if not r.hexists(hash,key):init_flag = True
        if init_flag :
            raise Exception('Redis字段异常，初始化Redis')

    except:
        print('初始化Redis数据库')

        r.lpush('ERROR_LOG', 0)

        r.set('base_delay',2.66)

        r.hset('Task_Flag','fengmo',0)
        r.hset('Task_Flag', 'yinjie', 0)
        r.hset('Task_Flag', 'yuhun', 0)
        r.hset('Task_Flag', 'fudai', 0)
        r.hset('Task_Flag', 'jiejie', 0)

        r.set('ERROR_FLAG',0)

        r.set('log_fight','{"date": "2024-08-07", "weekday": "3", "daily": [0, 0], "shui": [17, 0], "tu": [0, 0], "wang": [0, 0], "huo": [0, 0], "ri": [0, 0], "shi": [0, 0], "douji": [0, 0]}')

        r.set('Server_Switch', 0)

        r.set('Digui_Switch', 0)

        r.set('Jiyang_Flag', '2024-08-06 22:30:22')

        r.lpush('Jiyang_Log', 0)

        r.set('Speed_Flag', 1)

        r.set('Task_List',
              '{"weipai": [1, 1], "jiejie": [0, 0], "digui": [0, 0], "yuhun": [0, 0], "fengmo": [1, 0], "liaojinbi": [0, 0], "yinjie": [0, 0], "huahe": [1, 0]}')

        r.lpush('log_fight_his', 0)

        # r.set('daily', 0)

        r.hset('Task_Queue', 'yinjie', 0)
        r.hset('Task_Queue', 'weipai', 0)
        r.hset('Task_Queue', 'jiejie', 0)
        r.hset('Task_Queue', 'digui', 0)
        r.hset('Task_Queue', 'yuhun', 0)
        r.hset('Task_Queue', 'fengmo', 0)
        r.hset('Task_Queue', 'liaojinbi', 0)
        r.hset('Task_Queue', 'huahe', 0)
        r.hset('Task_Queue', 'daily', 0)

        r.hset('Taigu_Sum', '4', 0)
        r.hset('Taigu_Sum', '5', 0)
        r.hset('Taigu_Sum', '6', 0)

        r.hset('Huodong', 'flag', 0)
        r.hset('Huodong', 'time', 0)
        r.hset('Huodong', 'number', 0)
        r.hset('Huodong', 'finish', 0)





Check_Redis()