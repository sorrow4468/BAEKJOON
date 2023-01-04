N, M = map(int, input().split())
dictt = {}
for n in range(1, N+1):
    dictt[n] = set()
for _ in range(M):
    A, B = map(int, input().split())
    dictt[A].add(B)
    dictt[B].add(A)
for n in range(1, N+1):
    print(len(dictt[n]))

# N, M = map(int, input().split())
# arr = [set() for _ in range(N+1)]
# for m in range(M):
#     A, B = map(int, input().split())
#     arr[A].add(B)
#     arr[B].add(A)
# for n in range(1, N+1):
#     print(len(arr[n]))