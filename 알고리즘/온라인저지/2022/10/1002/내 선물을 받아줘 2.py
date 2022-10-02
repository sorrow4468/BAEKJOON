import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = input().rstrip()
result = 0
for i in range(N-1):
    tmp = arr[i] + arr[i+1]
    if tmp == 'EW': result += 1
print(result)