N, M = map(int, input().split())
J = int(input())
result, s, e = 0, 1, M
for j in range(J):
    A = int(input())
    if s<=A<=e: # 움직이지 않아도 될 때
        continue
    else: # 움직여야 할 때
        if A < s: # 좌로 움직일 때
            move = s-A
            result += move 
            s, e = s-move, e-move
        elif e < A: # 우로 움직일 때
            move = A-e
            result += move
            s, e = s+move, e+move
print(result)