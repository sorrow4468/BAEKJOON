N = int(input())
C = set(map(int, input().split()))
M = int(input())
for i in list(map(int, input().split())): print(1 if i in C else 0, end=' ')