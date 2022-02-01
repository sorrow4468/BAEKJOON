T = int(input())

for t in range(T):
    a, b = map(int, input().split())

    result = 1

    for i in range(b):
        result = (result*a)%10

    if result:
        print(result)
    else:
        print(10)