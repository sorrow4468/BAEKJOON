import sys

input = sys.stdin.readline

now = float(input().rstrip())
while True:
    D = float(input().rstrip())
    if D >= 999: break
    print('{:.2f}'.format(D-now))
    now = D