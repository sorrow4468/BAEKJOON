import sys

input = sys.stdin.readline

while True:
    tmp = input().rstrip()
    check = tmp[0]
    if check == '#': break
    sen = tmp[2:]
    result = 0
    for s in sen:
        if s.lower() == check:
            result += 1
    print(check, result)