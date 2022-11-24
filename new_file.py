# from datetime import time, datetime, timedelta, date, time


#
# today = date(2021, 11, 4)
# birthday = date(2022, 10, 6)
#
# days1 = birthday - today
#
# print(days1)
# h, m, s = map(int, input().split(':'))
# t = timedelta(hours=h, minutes=m, seconds=s)
# n = int(input())
# res = t + timedelta(seconds=n)
# print(f"{res.seconds// 3600}:{(res.seconds // 60) % 60}:{res.seconds % 60}")


# from datetime import date, timedelta
#
# today = date(2021, 11, 4)
# birthday = date(2022, 10, 6)
#
# days = birthday - today
#
# print(days.days)


# h, m, s = map(int, input().split(':'))
# n = int(input())
# t = datetime(1, 1, 1, hour=h, minute=m, second=s)
# r = t + timedelta(seconds=n)
# print(r.strftime('%H:%M:%S'))

# def num_of_sundays(year):
#     sp = 0
#     t = date(year=year, month=1, day=1)
#     t2 = date(year=year + 1, month=1, day=1)
#     for i in range(t.toordinal(), t2.toordinal()):
#         date1 = date.fromordinal(i)
#         if date1.isoweekday() == 7:
#             sp += 1
#     return sp
#
#
# print(num_of_sundays(768))
# a = list(map(int, input().split('.')))
# today = datetime(year=a[2], month=a[1], day=a[0])
# s = 0
# print(datetime.strftime(today, '%d.%m.%Y'))
# for i in range(2, 11):
#     s += i
#     delta = today + timedelta(days=s)
#
#     print(datetime.strftime(delta, '%d.%m.%Y'))
# dates = ['01.11.2021', '07.11.2021', '04.11.2021', '03.11.2021']
# def fill_up_missing_dates(d):
#     sp = []
#     for i in d:
#         day, month, year = i.split('.')
#         ma_date = datetime(int(year), int(month), int(day))
#         sp.append(ma_date)
#     sp1 = [date.fromordinal(i) for i in range(min(sp).toordinal(), max(sp).toordinal() + 1)]
#     sp2 = [datetime.strftime(i, '%d.%m.%Y')for i in sp1]
#     return sp2
# print(fill_up_missing_dates(dates))

# start = datetime.strptime(input(), '%H:%M')
# fin = datetime.strptime(input(), '%H:%M')
# while start + timedelta(minutes=45) <= fin:
#     st = start
#     start = start + timedelta(minutes=45)
#     print(f"{st.strftime('%H:%M')} - {start.strftime('%H:%M')}")
#     start = start + timedelta(minutes=10)
#


# 3.5 задача №1
# from datetime import date, time, datetime, timedelta
#
# data = [('07:14', '08:46'),
#         ('09:01', '09:37'),
#         ('10:00', '11:43'),
#         ('12:13', '13:49'),
#         ('15:00', '15:19'),
#         ('15:58', '17:24'),
#         ('17:57', '19:21'),
#         ('19:30', '19:59')]
#
# sum = timedelta(minutes=0)
# for i in data:
#     a = datetime.strptime(i[1], '%H:%M') - datetime.strptime(i[0], '%H:%M')
#     sum += a
#
# print(sum.seconds // 60)

#3.5 задача №2
from datetime import date, time, datetime, timedelta



#3.5 задача № 3


# a = input()
# date = datetime.strptime(a, "%d.%m.%Y %H:%M")
#
# if date.isoweekday() > 5:
#     t = date.time()
#     if t >= time(10, 0) and t <= time(18, 0):
#         res = date  - timedelta()
#         print(res)

#3.4 задача №4
date1 = datetime.strptime(input(), "%d.%m.%Y")
date2 = datetime.strptime(input(), "%d.%m.%Y")
sp = []
for i in range(date1.toordinal(), date2.toordinal() + 1):
    a = datetime.fromordinal(i)
    count = 0

    if sp = 0 and (a.month + a.day) % 2 != 0:
        print(a)
