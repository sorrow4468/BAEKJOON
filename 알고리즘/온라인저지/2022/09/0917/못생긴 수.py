import sys
from heapq import heappush, heappop

input = sys.stdin.readline

def ugly(num):
    result = 0
    HQ = []
    heappush(HQ, 1)
    cnt = 0
    while HQ:
        num = heappop(HQ)
        cnt += 1
        if cnt == N: 
            result = num
            break
        for i in (2, 3, 5):
            next = num*i
            if next not in HQ:
                heappush(HQ, next)
    return result

while True:
    N = int(input().rstrip())
    if N == 0: break
    print(ugly(N))

# http://www.jungol.co.kr/bbs/board.php?bo_table=pbank&code=1318&sca=4030