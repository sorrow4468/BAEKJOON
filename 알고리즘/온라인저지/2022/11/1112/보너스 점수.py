import sys

input = sys.stdin.readline

N = int(input().rstrip())
answer = input().rstrip()
result = 0
bonus = 0
for i in range(N):
    if answer[i] == 'X':
        bonus = 0
    elif answer[i] == 'O':
        result += i+1
        result += bonus
        bonus += 1
        # print(bonus)
print(result)
    