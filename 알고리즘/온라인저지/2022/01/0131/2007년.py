"""
1월 1일은 월요일
x월y일이 1년중 몇번째 날인지 구해서
mod 7
"""

x, y = map(int, input().split())

day = y-1

if x > 1:
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for i in range(x-1):
        day += month[i]

week = ['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN']

weekday = day % 7

print(week[weekday])