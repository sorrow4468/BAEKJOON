d = [0] * 42
for _ in range(10):
    n = int(input())
    d[n%42] = 1
print(sum(d))