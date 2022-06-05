N = int(input())
# N = 3
if N == 1:
    tmp = ['*']
else:
    if N%2:
        tmp = [['*']*((N//2)+1), ['']+['*']*(N//2)]
    else:
        tmp = [['*']*(N//2), ['']+['*']*(N//2)]
for i in range(N):
    for t in tmp:
        print(*t)
    