N, S, R = map(int, input().split())
crack = list(map(int, input().split()))
spare = list(map(int, input().split()))
K = [True] * N # kayak
for c in crack:
    K[c-1] = False
for s in spare:
    try:
        if not K[s-1]: K[s-1] = True
        elif not K[s-2]: K[s-2] = True
        elif not K[s]: K[s] = True
    except:
        pass
result = 0
for k in K:
    if not k:
        result += 1
print(result)