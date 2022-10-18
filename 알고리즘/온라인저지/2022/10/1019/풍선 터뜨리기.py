import sys
from collections import deque

input = sys.stdin.readline
N = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))
Q = deque()
for i in range(1, N+1): Q.append((i, arr[i-1]))
while True:
    idx, move = Q.popleft()
    print(idx, end=' ')
    if not Q: break
    if move > 0:
        for i in range(move-1):
            Q.append(Q.popleft())
    else:
        for i in range(abs(move)):
            Q.appendleft(Q.pop())