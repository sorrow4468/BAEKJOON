N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[0], x[1]))
for a in arr: print(*a)