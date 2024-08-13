from datetime import date
day_now = date.today()
print(day_now)

xday = date(2000, 8, 26)
td = day_now - xday
print(td)
