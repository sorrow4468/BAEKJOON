import sys

def change(num):
    if switch[num]:
        switch[num] = 0
    else:
        switch[num] = 1
    return

switch_count = int(sys.stdin.readline())
switch = [-1] + list(map(int, sys.stdin.readline().split()))
students = int(sys.stdin.readline())

for i in range(students):
    sex, num = map(int, sys.stdin.readline().split())
    if sex == 1:
        for j in range(num, switch_count+1, num):
            change(j)
    else:
        change(num)
        for k in range(switch_count//2):
            if num+k > switch_count or num - k < 1:
                break
            if switch[num+k] == switch[num-k]:
                change(num+k)
                change(num-k)
            else:
                break

for i in range(1, len(switch)):
    print(switch[i], end=' ')
    if not i%20:
        print()
