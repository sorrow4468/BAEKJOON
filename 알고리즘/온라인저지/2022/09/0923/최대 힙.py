import sys
from heapq import heappush, heappop

input = sys.stdin.readline

HQ = []
for _ in range(int(input().rstrip())):
    num = int(input().rstrip())
    if num: heappush(HQ, (-num, num))
    else: 
        if HQ: print(heappop(HQ)[1])
        else: print(0)