import sys

input = sys.stdin.readline

N = input().rstrip()
flag = False
for i in range(1, len(N)):
    A, B = N[:i], N[i:]
    front, rear = 1, 1
    for a in A:
        front *= int(a)
    for b in B:
        rear *= int(b)
    if front == rear: flag = True; break
print('YES' if flag else 'NO')