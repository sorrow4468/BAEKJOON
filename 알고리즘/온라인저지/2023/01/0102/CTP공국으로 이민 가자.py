for tc in range(int(input())-1, -1, -1):
    input()
    for i in input().split():
        try:
            print(chr(int(i)+64), end=' ')
        except:
            print(ord(i)-64, end=' ')
    if tc: print()