for _ in range(3):
    N = int(input())
    tmp = [int(input()) for __ in range(N)]
    result = '0'
    if sum(tmp) > 0: result = '+'
    elif sum(tmp) < 0: result = '-'
    print(result)