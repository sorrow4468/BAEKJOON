for _ in range(int(input())):
    result = sum(list(range(65, 91)))
    for i in input():
        result -= ord(i)
    print(result)
