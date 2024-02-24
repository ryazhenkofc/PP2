import datetime

today = datetime.date.today()
diff = datetime.timedelta(days = 1)
print(f'Yesterday: {today-diff}')
print(f'Today: {today}')
print(f'Tomorrow: {today+diff}')