i = 0

N, M, K = map(int, input().split())

seat_found = False

for n in range(N):
    for m in range(M):
        if i == K:
            print(n, m)
            seat_found = True
            break

        i += 1
    
    if seat_found:
        break