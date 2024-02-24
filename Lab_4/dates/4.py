import datetime

today = datetime.date.today()
day = datetime.timedelta(days = 3)
y = today + day

t = y - today

print(t.days * 86400)