def oct_to_bin(x):
    global result
    dictt = {
        '0': '000',
        '1': '001',
        '2': '010',
        '3': '011',
        '4': '100',
        '5': '101',
        '6': '110',
        '7': '111',
    }
    # print(dictt[x])
    return dictt[x]

N = input()
if N == '0':
    print(0)
    exit()
# print(N, len(N))
result = [''] * (len(N))
# print(result)
for i in range(len(N)):
    result[i] = oct_to_bin(N[i])
    # print(result)
print(result[0].lstrip('0'), end='')
for r in result[1:]:
    print(r, end='')