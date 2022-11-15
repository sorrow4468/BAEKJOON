import sys

input = sys.stdin.readline

octopus = {
    '-': 0,
    '\\': 1,
    '(': 2,
    '@': 3,
    '?': 4,
    '>': 5,
    '&': 6,
    '%': 7,
    '/': -1,
}

while True:
    tmp = list(input().rstrip())[::-1]
    if tmp == ['#']: break
    j = 0
    result = 0
    for i in range(len(tmp)):
        result += 8**j*octopus[tmp[i]]
        j += 1
    print(result)