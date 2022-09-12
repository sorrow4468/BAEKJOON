data = []
for _ in range(3):
    data.append(int(input()))
if sum(data) == 180:
    if data[0] == data[1] and data[1] == data[2] and data[2] == data[0]:
        print('Equilateral')
    elif data[0] == data[1] or data[1] == data[2] or data[2] == data[0]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')