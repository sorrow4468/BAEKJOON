import sys

input = sys.stdin.readline

def enough(money):
    money_in_hand, draw = money, 1
    for a in arr:
        if money_in_hand>=a: money_in_hand -= a
        else:
            draw += 1
            money_in_hand = money-a
    if draw<=M: return True
    return False

N, M = map(int, input().rstrip().split())
arr = [int(input()) for _ in range(N)]
result = int(1e9)
start, end = max(arr), result
while start<=end:
    mid = (start+end) // 2
    if enough(mid):
        result = min(result, mid)
        end = mid-1
    else: start = mid+1
print(result)

# https://www.acmicpc.net/problem/6236