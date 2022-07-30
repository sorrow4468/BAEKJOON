N, M = map(int, input().split())
S_min = P_min = 1e9 # set min, piece min
for m in range(M):
    S, P = map(int, input().split()) # set, piece
    if S < S_min: S_min = S
    if P < P_min: P_min = P
    if P*6 < S_min: S_min = P*6
result = N//6 * S_min
result += min(N%6 * P_min, S_min)
print(result)