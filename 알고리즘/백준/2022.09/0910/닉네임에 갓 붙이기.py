for _ in range(int(input())):
    nickname = input().split()
    for i in ['god'] + nickname[1:]:
        print(i, end='')
    print()