from datetime import datetime, date


def what_day_is_it(date):
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    day = date.weekday()
    print(days[day])

D, M = map(int, input().split())
what_day_is_it(date(2009, M, D))