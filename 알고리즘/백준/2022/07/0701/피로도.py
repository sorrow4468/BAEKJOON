A, B, C, M = map(int, input().split())
result = 0
F = 0 # fatigue : 피로도
if not A > M:
    for i in range(24):
        if F+A <= M:
            F += A
            result += B
        else:
            F -= C
            if F < 0:
                F = 0
print(result)