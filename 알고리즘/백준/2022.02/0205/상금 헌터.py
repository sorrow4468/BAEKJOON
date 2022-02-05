prizes1 = [
    [1, 5000000],
    [3, 3000000],
    [6, 2000000],
    [10, 500000],
    [15, 300000],
    [21, 100000]
]

prizes2 = [
    [1, 5120000],
    [3, 2560000],
    [7, 1280000],
    [15, 640000],
    [31, 320000]
]

T = int(input())

for t in range(T):    
    a, b = map(int, input().split())

    prize = 0
    
    if 0 < a <= 21:
        for p in prizes1:
            if a <= p[0]:
                prize += p[1]
                break

    if 0 < b <= 31:
        for p in prizes2:
            if b <= p[0]:
                prize += p[1]
                break

    print(prize)