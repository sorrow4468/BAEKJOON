a, b = map(int, input().split())
c, d = a, b
while a % b != 0:
    a, b = b, a % b

print(b)
print(b*(c//b)*(d//b))