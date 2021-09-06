import sys
def input():
    return sys.stdin.readline()

X = int(input())
bars = [64, 32, 16, 8, 4, 2, 1]
i = 0
cnt = 0
while X != 0:
    if X >= bars[i]:
        X -= bars[i]
        cnt += 1
    else:
        i += 1
print(cnt)