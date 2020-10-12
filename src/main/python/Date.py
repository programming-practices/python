
from datetime import datetime
from datetime import timedelta

# print(dir(datetime))
# print(datetime.datetime.now())

hoy = datetime.now()

# print(timedelta(days=2))
# print(hoy - timedelta(days=2))

# print(hoy)
# print(hoy - delta(date = 1))
#
# print(hoy.strftime("%d"))
# print(hoy.strftime("%b"))
# print(hoy.strftime("%Y"))
# print(hoy.strftime("%s"))
# print(hoy.strftime("%S"))
# print(hoy.strftime("%Y - %m - %d"))
# print(hoy.strftime("%Y - %b - %d"))

# date_2018_7_30 = datetime(2018, 7, 30)
# i = 29
# while i >= 0:
#     day = date_2018_7_30 - timedelta(i)
#     if day.day % 2 == 0:
#         print(day.day)
#     i -= 1

# today = datetime.utcnow()
# first = today.replace(day=1)
# print(today)
# print(first)
# i = 0
# while i < 30:
#     day = first - timedelta(days=i)
#     daynum = int(day.strftime("%e"))
#     if daynum%2 == 0:
#         print(day.strftime("%A %e %B %Y"))
#     i += 1

day_2018_6_1 = datetime(2018, 6, 1)
i = 1
while i <= 30:
    if i % 2 == 0:
        date = datetime(2018, 6, i)
        print(date)
    i += 1
