N = int(input())
arr = [tuple(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[1], x[0]))
for a in arr: print(*a)