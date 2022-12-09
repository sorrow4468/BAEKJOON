def mix(order):
    if order == 'A':
        result[0], result[1] = result[1], result[0]
    elif order == 'B':
        result[0], result[2] = result[2], result[0]
    elif order == 'C':
        result[0], result[3] = result[3], result[0]
    elif order == 'D':
        result[2], result[1] = result[1], result[2]
    elif order == 'E':
        result[3], result[1] = result[1], result[3]
    elif order == 'F':
        result[2], result[3] = result[3], result[2]

result = [1, 0, 0, 2]
for order in input():
    mix(order)
print(result.index(1)+1)
print(result.index(2)+1)