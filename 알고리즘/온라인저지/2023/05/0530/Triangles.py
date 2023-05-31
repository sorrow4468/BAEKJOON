while True:
    N = int(input())
    if not N:
        break
    line = '*'
    for i in range(N):
        print(line)
        line += '*'