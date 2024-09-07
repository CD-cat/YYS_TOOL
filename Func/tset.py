import redis,datetime,os
import redis
import json,time


with open("../Redis_Info.txt", "r") as f:  # 打开文件
    data = f.read()  # 读取文件
    print(data)
d = json.loads(data)
a = 'localhost'
b = 6379
c = 0
d = [a,b,c]
d_str = json.dumps(d)

with open("../Redis_Info.txt", "w") as f:  # 打开文件
        f.write(d_str)
r = redis.StrictRedis(host=d[0], port=d[1], db=d[2])
a = r.get('log_fight')
b = a[-1]
print(b)


# file_path = "./data/game_data/Redis_Backup.txt"
#
# redis_conn = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)
# data_keys = redis_conn.keys()
#
# all_data = {}
# for i in data_keys:
#     n = redis_conn.get(i)
#     all_data[i] = json.loads(n)
#
#
# file_object = open(file_path, 'w', encoding="utf8")
# json.dump(all_data, file_object, ensure_ascii=False)
#
# file_object.close()



# DATA_ROOT = r'D:\0.project\5.YYS_Tool\data'
# c = os.getcwd()
# # c.replace('\\\\','\\')
# c = c.replace('Func','data')
# if c == DATA_ROOT:
#     print('yeeeee')
# b = int(r.hget('Task_Queue','yinjie'))
# print(b)
# r.hset('Task_Queue','yinjie',1)
# # r.hget('Task_Queue','yinjie')
#
# a = r.hkeys('Task_Queue')
# for i in a:
#     print(r.hget('Task_Queue',i))
#     r.hset('Task_Queue',i,0)
# b = r.hset('Taigu_Sum', '6', '1')
# c = r.hget('Taigu_Sum',4)
# print(a)
# print(b)
# print(c)


# base_delay = float(r.get('base_delay').decode('utf-8'))
# time1 = datetime.datetime.now()
# now_time = time1.strftime('%Y-%m-%d %H:%M:%S')
# r.set('Jiyang_Flag',now_time)
# print(base_delay)
# print(type(r.get('ex')))
# list = r.get('Task_List').decode('utf-8')
# list1 = json.loads(list)
# print(r.get('ex'))
# print(type(r.get('ex')))

# r.close()

