import sys

input = sys.stdin.readline

triangle = [1]
for i in range(2, 1000):
    tmp = triangle[-1]+i
    if tmp<=1000: triangle.append(tmp)
    else: break
result = set()
len_tri = len(triangle)
for i in range(len_tri):
    for j in range(len_tri):
        for k in range(len_tri):
            tmp = triangle[i]+triangle[j]+triangle[k]
            if tmp<=1000: result.add(tmp)
for _ in range(int(input().rstrip())):
    K = int(input().rstrip())
    print(1 if K in result else 0)