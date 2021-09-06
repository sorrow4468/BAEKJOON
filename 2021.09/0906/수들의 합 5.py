import sys
def input():
    return sys.stdin.readline()

N = int(input())
cnt = 0
for n in range(1, N+1):
    tmp = N
    for i in range(n, N+1):
        tmp -= i
        if tmp < 0:
            break
        elif not tmp:
            cnt += 1
            break
print(cnt)