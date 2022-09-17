import sys
N = int(sys.stdin.readline())

layer = 1
i = 1
while layer < N:
    i += 1
    layer += (i-1)*6
print(i)