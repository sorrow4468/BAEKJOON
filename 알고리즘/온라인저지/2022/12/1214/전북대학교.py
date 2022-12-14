N = int(input())
if not N%2:
    print('I LOVE CBNU')
else:
    print('*'*N)
    space = N//2
    print(' '*space + '*')
    for _ in range(N//2):
        space -= 1
        print(' '*space + '*'+' '*(((N//2)-space)*2-1)+'*')