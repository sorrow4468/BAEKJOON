num = input()
A = B = 0
if len(num) == 2:
    A = int(num[0])
    B = int(num[1])
elif len(num) == 3:
    if num[1] == '0':
        A = int(num[:2])
        B = int(num[-1])
    elif num[-1] == '0':
        A = int(num[0])
        B = int(num[1:])
else: # len 4
    A = int(num[:2])
    B = int(num[2:])
# print(A, B)
print(A+B)

