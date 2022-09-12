import math

for t in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    D = math.sqrt((x1-x2)**2 + (y1-y2)**2) # distance
    result = 0
    if D == 0 and r1 == r2: result = -1
    elif D == abs(r1-r2) or D == r1+r2: result = 1
    elif abs(r1-r2) < D < r1+r2: result = 2
    print(result)

"""
일치
내접or외접
두 점에서 접함
접점이 없음
"""