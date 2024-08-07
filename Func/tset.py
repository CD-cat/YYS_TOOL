import redis,datetime,os



r = redis.StrictRedis(host='localhost', port=6379, db=0)
DATA_ROOT = r'D:\0.project\5.YYS_Tool\data'
c = os.getcwd()
# c.replace('\\\\','\\')
c = c.replace('Func','data')
if c == DATA_ROOT:
    print('yeeeee')
b = int(r.hget('Task_Queue','yinjie'))
print(b)
r.hset('Task_Queue','yinjie',1)
# r.hget('Task_Queue','yinjie')

a = r.hkeys('Task_Queue')
for i in a:
    print(r.hget('Task_Queue',i))
    r.hset('Task_Queue',i,0)
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

