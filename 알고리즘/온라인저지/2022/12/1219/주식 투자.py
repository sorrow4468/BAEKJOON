for _ in range(int(input())):
    result = 0
    for n in range(int(input())):
        result += max(list(map(int, input().split())) + [0])
    print(result)