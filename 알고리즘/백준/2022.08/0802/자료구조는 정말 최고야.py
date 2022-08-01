import sys

input = sys.stdin.readline

N, M = map(int, input().split())
result = True
for _ in range(M):
    K = int(input())
    B = list(map(int, input().split()))
    for k in range(K-1):
        if B[k] < B[k+1]: # 한 권의 책이라도 오름차순이 아니면 정답이 될 수 없다
            result = False
            break
    if not result: break
print('Yes' if result else 'No')