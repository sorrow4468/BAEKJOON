def hanoi(N, a, b, c):
    if N == 1:
        print(a, c)
    else:
        hanoi(N-1, a, c, b)
        print(a, c)
        hanoi(N-1, b, a, c)

N = int(input())
print(2**N-1) # 하노이의 탑 이동횟수 일반항 2**n - 1
hanoi(N, 1, 2, 3)

# https://www.acmicpc.net/problem/11729