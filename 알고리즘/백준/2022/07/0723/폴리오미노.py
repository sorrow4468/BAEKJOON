board = input().split('.')
# print(board)
result = ''
for i in range(len(board)):
    if len(board[i])%2:
        result = -1
        break
    result += 'AAAA' * (len(board[i])//4)
    if len(board[i])%4:
        result += 'BB'
    if i != len(board)-1:
        result += '.'
    # if b == '':
    #     result += '.'
print(result)