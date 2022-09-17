N, X, K = map(int, input().split())
cups = [0] * N
cups[X-1] = 1
# print(cups)
for k in range(K):
    A, B = map(int, input().split())
    cups[A-1], cups[B-1] = cups[B-1], cups[A-1]
# print(cups)
print(cups.index(1)+1)