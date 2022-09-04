N = input()
tmp = 0
zero = False
result = []
for n in N:
    n = int(n)
    tmp += n
    result.append(n)
    if n == 0: zero = True
tmp %= 3
result.sort(reverse=True)
if not tmp and zero:
    for r in result:
        print(r, end='')
else:
    print(-1)