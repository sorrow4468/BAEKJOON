import sys

input = sys.stdin.readline

N = int(input().rstrip())
M = int(input().rstrip())
parts = sorted(list(map(int, input().rstrip().split())))
i, j = 0, N-1 # j = len(parts)-1
result = 0
while i < j:
    armor = parts[i] + parts[j]
    if armor > M: j -= 1
    elif armor < M: i += 1
    else: # armor == M
        result += 1
        i += 1
print(result)