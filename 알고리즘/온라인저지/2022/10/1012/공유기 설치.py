import sys

input = sys.stdin.readline

def install(distance):
    prev = houses[0]
    cnt = 1
    for house in houses[1:]:
        if house>=prev+distance:
            cnt += 1
            prev = house
    return cnt

N, C = map(int, input().rstrip().split())
houses = sorted([int(input().rstrip()) for _ in range(N)])
start, end = 0, houses[-1]-houses[0]
result = 1
while start<=end:
    mid = (start+end) // 2
    if install(mid)>=C:
        result = max(result, mid)
        start = mid+1
    else: end = mid-1
print(result)