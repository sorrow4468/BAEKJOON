import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = [input().rstrip() for _ in range(N)]
friend_2 = [[] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'Y':
            if j not in friend_2[i]:
                friend_2[i].append(j)
            if i not in friend_2[j]:
                friend_2[j].append(i)
            for k in range(N):
                if arr[j][k] == 'Y' and i != k:
                    if k not in friend_2[i]:
                        friend_2[i].append(k)
                    if i not in friend_2[k]:
                        friend_2[k].append(i)
result = 0
for friend in friend_2: result = max(result, len(friend))
print(result)