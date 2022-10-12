import sys

input = sys.stdin.readline

N, M = int(input().rstrip()), int(input().rstrip())
result = set()
friends = [[] for _ in range(N+1)]
for m in range(M):
    a, b = map(int, input().rstrip().split())
    friends[a].append(b)
    friends[b].append(a)
for friend in friends[1]:
    if friend != 1: result.add(friend)
    for f in friends[friend]:
        if f != 1: result.add(f)
print(len(result))