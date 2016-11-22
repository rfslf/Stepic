import datetime

a = datetime.datetime.strptime(input(), "%Y %m %d")
d = datetime.timedelta(days=int(input()))
a = a + d
print(a.year, a.month, a.day)