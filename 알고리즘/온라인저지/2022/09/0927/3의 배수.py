import sys

input = sys.stdin.readline

X = input().rstrip()
result = 0
while len(X)>1:
    tmp = 0
    for x in X:
        tmp += int(x)
    X = str(tmp)
    result += 1
print(result)
print('NO' if int(X)%3 else 'YES')