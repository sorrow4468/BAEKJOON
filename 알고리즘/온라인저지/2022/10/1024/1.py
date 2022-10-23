import sys

input = sys.stdin.readline

while True:
    try:
        N = int(input().rstrip())
        num = ''
        while True:
            num += '1'
            if not int(num)%N:
                print(len(num))
                break
    except:
        break