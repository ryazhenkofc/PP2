import datetime

today = datetime.datetime.today()
diff = datetime.timedelta(microseconds=today.microsecond)
today -= diff

print(today)