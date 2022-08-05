N = int(input())
for n in range(1, N+1):
    T = sorted(list(map(int, input().split()))) # triangle
    print(f'Scenario #{n}:')
    if T[0]**2 + T[1]**2 == T[2]**2: print('yes\n')
    else: print('no\n')        