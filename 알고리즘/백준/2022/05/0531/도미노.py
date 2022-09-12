a = 0
result = 0
for i in range(int(input()), -1, -1):
    a += 3
    result += i*a
print(result)

"""
2 = 0+1+2 = 0+3+9
3=0+1+2+3 = 0+3+9+18 = 0+3+(3+6)+(3+6+9)

"""