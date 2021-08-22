r, g, b = map(int, input().split())
    # map(int, input().split()) = 이건 거의 공식이다
    # 받은 인자를 공백을 기준으로 나눠서 int로 저장
for i in range(r):
    for j in range(g):
        for k in range(b):
            print(i, j, k)
print(r * g * b)