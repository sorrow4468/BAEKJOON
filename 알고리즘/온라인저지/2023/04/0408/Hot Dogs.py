while True:
    try:
        A, B = map(int, input().split())
        print(f'{A/B:.2f}')
    except EOFError:
        break