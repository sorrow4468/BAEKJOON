L, P = map(int, input().split())

a = list(map(int, input().split()))

s = L * P

for i in a:
    print(i-s, end=' ')