from datetime import datetime


now  = datetime.now()

print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)

timestamp = datetime.timestamp(datetime.now())

print(timestamp)

year_2023 = datetime(2023, 1, 1)

def print_date(date):
    print(date.year)
    print(date.month)
    print(date.day)
    print(date.hour)
    print(date.minute)
    print(date.second)

print_date(year_2023)

from datetime import time

current_time = time(21,6,0)

print(current_time)

from datetime import date

current_time = date(21,6,1)

print(current_time.year)
print(current_time.month)
print(current_time.day)

current_time = date(current_time.year, current_time.month + 1, current_time.day)

print(current_time)

diff = year_2023.date() - current_time
print(diff)

from datetime import timedelta

start_timedelta = timedelta(200, 100, 100, weeks=10)
end_timedelta = timedelta(300, 100, 100, weeks=13)

print( end_timedelta + start_timedelta)
print( end_timedelta + start_timedelta)