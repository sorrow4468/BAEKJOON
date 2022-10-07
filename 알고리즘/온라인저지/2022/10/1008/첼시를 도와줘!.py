import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    P = int(input().rstrip())
    cost, name = [], []
    for p in range(P):
        player = input().rstrip().split()
        cost.append(int(player[0]))
        name.append(player[1])
    result = [0, 0]
    for i in range(P):
        if cost[i] > result[0]:
            result[0] = cost[i]
            result[1] = i
    print(name[result[1]])