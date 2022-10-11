import sys

input = sys.stdin.readline

N = int(input().rstrip())
result = 0
num = 1
while N:
    result += 1
    if num > N: num = 1
    N -= num
    num += 1
print(result)