a, b = map(int, input().split())
cheap = b/a
e, f = a, b
N = int(input())
for n in range(N):
    c, d = map(int, input().split())
    if d/c > cheap:
        cheap = d/c
        e, f = c, d
# print(e, f)
print(f'{e*1000/f:.2f}')
# 37:532 = x:1000