import sys

input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
nums = list(map(int, input().rstrip().split()))
sett = set()
result = 0
for num in nums:
    for i in range(num, N+1, num):
        if i not in sett: result += i
        sett.add(i)
print(result)