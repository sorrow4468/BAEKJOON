import sys

input = sys.stdin.readline

N = int(input().rstrip())
D = 9
sep = []
while True:
    if N >= D:
        sep.append(D)
        N -= D
        D *= 10
    else:
        sep.append(N)
        break
result = 0
i = 1
for s in sep: 
    result += i*s
    i += 1
print(result)