import sys

input = sys.stdin.readline

result = [[0]*5 for _ in range(3)]
for i in range(3): result[i][4] = i+1
for _ in range(int(input().rstrip())):
    A, B, C = map(int, input().rstrip().split())
    result[0][0] += A
    result[1][0] += B
    result[2][0] += C
    result[0][A] += 1
    result[1][B] += 1
    result[2][C] += 1
result.sort(key=lambda x:(-x[0], -x[3], -x[2], -x[1]))
if result[0][:4] == result[1][:4]:
    print(0, result[0][0])
else: print(result[0][4], result[0][0])