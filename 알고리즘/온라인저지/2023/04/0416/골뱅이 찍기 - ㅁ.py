N = int(input())
for _ in range(N):
    print('@'*5*N)

for _ in range(3):
    for _ in range(N):
        print('@'*N + ' '*N*3 + '@'*N)

for _ in range(N):
    print('@'*5*N)