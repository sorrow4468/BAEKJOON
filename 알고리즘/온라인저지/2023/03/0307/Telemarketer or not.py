A = int(input())
B = int(input())
C = int(input())
D = int(input())
result = 0
if A == 8 or A == 9:
    if D == 8 or D == 9:
        if C == B:
            result = 1
print('ignore' if result else 'answer')