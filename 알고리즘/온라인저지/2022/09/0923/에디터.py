import sys

input = sys.stdin.readline

left = list(input().rstrip())
right = []
# 커서의 이동을 좌우 스택간에 이동으로 구현
for _ in range(int(input().rstrip())):
    order = input().rstrip().split()
    if order[0] == 'L' and left: right.append(left.pop())
    elif order[0] == 'D' and right: left.append(right.pop())
    elif order[0] == 'B' and left: left.pop()
    elif order[0] == 'P': left.append(order[1])
for a in left+list(reversed(right)): print(a, end='')

# https://www.acmicpc.net/problem/1406