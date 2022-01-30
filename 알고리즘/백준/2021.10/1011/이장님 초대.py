"""
1. 묘목 하나 심는데 1일
2. 묘목 n개 구입 -> n일
3. 이장님을 초대하기위해, 대신 묘목들이 완전히 자란 후에
    이장님을 초대하기 위한 최소 시간

1. 묘목의 수
2. 각 묘목별 걸리는 시간

1. 4 3 3 2 -> 
2. 39 39 38 35 20 9

2 3 4 5 ....

값을 정렬하고
for문 돌려서
range(2, N) 더해주고
max
"""

N = int(input())
trees = list(map(int, input().split()))

trees.sort(reverse=True)

j = 0

for i in range(2, 2+N):
    trees[j] += i
    j += 1

print(max(trees))