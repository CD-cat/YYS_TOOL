import redis

def Check_Redis():
    try:
        r = redis.StrictRedis(host='localhost', port=6379, db=0)
        a = r.get('base_delay').decode('utf-8')
        print(a)
    except:
        print('初始化Redis数据库')

        r.lpush('ERROR_LOG', 0)

        r.set('base_delay',2.66)

        r.hset('Task_Flag','fengmo',0)
        r.hset('Task_Flag', 'yinjie', 0)
        r.hset('Task_Flag', 'yuhun', 0)
        r.hset('Task_Flag', 'fudai', 0)

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

        r.set('daily', 0)

        r.hset('Task_Queue', 'yinjie', 0)
        r.hset('Task_Queue', 'weipai', 0)
        r.hset('Task_Queue', 'jiejie', 0)
        r.hset('Task_Queue', 'digui', 0)
        r.hset('Task_Queue', 'yuhun', 0)
        r.hset('Task_Queue', 'fengmo', 0)
        r.hset('Task_Queue', 'liaojinbi', 0)
        r.hset('Task_Queue', 'huahe', 0)

        r.hset('Taigu_Sum', '4', 0)
        r.hset('Taigu_Sum', '5', 0)
        r.hset('Taigu_Sum', '6', 0)





Check_Redis()