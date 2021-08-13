T = int(input())
for t in range(T):
    R, word = input().split()
    R = int(R)
    for wor in word:
        print(wor*R, end='')
    print()