T = int(input())
for t in range(1, T+1):
    sentence = list(input().split())
    sentence = sentence[::-1]
    print(f'Case #{t}: ', end='')
    for sen in sentence:
        print(sen, end=' ')
    print()
