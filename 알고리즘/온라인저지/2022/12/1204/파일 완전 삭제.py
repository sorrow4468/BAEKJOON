N = int(input())
files = list(map(int, list(input())))
result = ''
for i in range(len(files)):
    if N%2:
        result += str(int(not files[i]))
    else:
        result += str(files[i])
tmp = input()
if result == tmp:
    print('Deletion succeeded')
else:
    print('Deletion failed')