N = int(input())

for n in range(N):
    text = input()

    for i in range(len(text)):
        if i == 0:
            print(text[i].upper(), end='')
            continue
        print(text[i], end='')
    
    print()