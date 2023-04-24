N, M = map(int, input().split())
a = 100-N
b = 100-M
c = 100-(a+b)
d = a*b
q, r = 0, d
if d>=100:
    q = d//100
    r = d%100
print(a, b, c, d, q, r)
print(c+q, r)