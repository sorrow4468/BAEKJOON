N = int(input())
for k in range(1, 10101):
    if eval('k**2 + k + 1') == N:
        print(k)
        break