import time

print(time.time())
print((time.time() / (24 * 60 * 60 * 365)) + 1970)

print(time.localtime())

t = time.time()
result = time.ctime(t)
print(result)

t_tuple = time.localtime()
result = time.asctime(t_tuple)
print(result)

result = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print(result)

# pt = time.strptime("%Y-%m-%d %H:%M:%S","2018-06-19 11:30:02")


# while True:
#     print("111")
#     time.sleep(1)


import calendar

print(calendar.month(2017, 6))

# 获取当天日期
import datetime

t = datetime.datetime.now()
print(datetime.datetime.today())
print(datetime.datetime.now())

print(t.year)
print(t.month)
print(t.day)
print(t.hour)
print(t.minute)
print(t.second)

t = datetime.datetime.today()
# 获取7天后的日期
print(t + datetime.timedelta(days=7))

fist = datetime.datetime(2018,8,8,8,8,8)
print(fist)


