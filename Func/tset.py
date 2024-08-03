import redis,datetime


r = redis.StrictRedis(host='localhost', port=6379, db=0)
base_delay = float(r.get('base_delay').decode('utf-8'))
time1 = datetime.datetime.now()
now_time = time1.strftime('%Y-%m-%d %H:%M:%S')
r.set('Jiyang_Flag',now_time)
print(base_delay)
# print(type(r.get('ex')))
# list = r.get('Task_List').decode('utf-8')
# list1 = json.loads(list)
# print(r.get('ex'))
# print(type(r.get('ex')))

# r.close()

