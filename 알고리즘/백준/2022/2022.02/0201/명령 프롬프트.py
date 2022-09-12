N = int(input())

inputs = [''] * N

for i in range(N):
    inputs[i] = input()

for i in range(len(inputs[0])):
    flag = True
    word = inputs[0][i]

    for j in range(N):
        if word != inputs[j][i]:
            flag = False
            break
    
    if flag:
        print(word, end='')
    else:
        print('?', end='')
