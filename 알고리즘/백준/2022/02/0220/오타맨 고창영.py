T = int(input())

for t in range(T):
    typo, word = input().split()
    typo = int(typo)

    for i in range(len(word)):
        if i == typo-1:
            continue
        
        print(word[i], end='')
    print()