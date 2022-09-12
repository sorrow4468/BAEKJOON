N, M = map(int, input().split())
ball = [i for i in range(N+1)]
for m in range(M):
    i, j = map(int, input().split())
    ball[i], ball[j] = ball[j], ball[i]
print(*ball[1:])