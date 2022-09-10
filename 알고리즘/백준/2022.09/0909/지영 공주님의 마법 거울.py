N = int(input())
arr = [input() for _ in range(N)]
K = int(input())
if K == 1:
    for a in arr: print(a)
elif K == 2:
    for a in arr: print(a[::-1])
else:
    for a in arr[::-1]:
        print(a)