import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    number = input().rstrip()
    front = number[:3]
    rear = number[4:]
    tmp = 0
    j = 0
    for f in front[::-1]:
        tmp += 26**j*(ord(f)-65)
        j += 1
    print('nice' if abs(tmp-int(rear)) <= 100 else 'not nice')