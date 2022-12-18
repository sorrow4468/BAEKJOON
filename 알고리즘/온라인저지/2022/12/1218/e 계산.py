print('n e')
print('- -----------')
for n in range(10):
    e = 0
    for i in range(n+1):
        factorial = 1
        s = 1
        for f in range(1, i+1):
            factorial *= f
        s /= factorial
        e += s
    print(n, end=' ')
    e = str(e).split('.')
    print(f'{float(".".join(e)):0.9f}' if len(e[1]) > 9 else ".".join(e) if e[1] != '0' else e[0])