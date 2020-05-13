# 内建时间模块

from datetime import datetime, timedelta

now = datetime.now()
print(now)
# 2020-05-13 09:57:02.474927

dt = datetime(2020, 2, 20, 20, 20)
# 用指定日期时间创建datetime
print(dt)
# 2020-02-20 20:20:00


# datetime转换为timestamp
print(dt.timestamp())
# 1582201200.0
# Python的timestamp是一个浮点数。如果有小数位，小数位表示毫秒数。


# timestamp转换为datetime
t = 1582201200.0
print(datetime.fromtimestamp(t))
# 2020-02-20 20:20:00


# str转换为datetime
cday = datetime.strptime('2020-05-13 10:24:00', '%Y-%m-%d %H:%M:%S')
print(cday)
# 2020-05-13 10:24:00


# datetime转换为str
now = datetime.now()
print(now.strftime('%a, %b, %d %H:%M'))
# Wed, May, 13 10:29


# datetime加减
now = datetime.now()
print(now)
print(now + timedelta(hours=10))
print(now - timedelta(days=1))
print(now + timedelta(days=1, hours=12))
