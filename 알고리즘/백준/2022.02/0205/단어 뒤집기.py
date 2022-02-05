T = int(input())

for t in range(T):
    sen = input().split()

    for s in sen:
        print(s[::-1], end=' ')
    
    print()
