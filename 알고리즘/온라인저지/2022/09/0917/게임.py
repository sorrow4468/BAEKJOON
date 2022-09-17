import sys

input = sys.stdin.readline

X, Y = map(int, input().rstrip().split())
Z = int((Y*100/X))
result = -1
start, end = 1, int(1e9)
while start<=end:
    mid = (start+end) // 2
    new_win_rate = int(((Y+mid)*100/(X+mid)))
    if new_win_rate>Z:
        result = mid
        end = mid-1
    else: start = mid+1
print(result)

# https://www.acmicpc.net/problem/1072