import sys

input = sys.stdin.readline

N = int(input().rstrip())
mid = 1+2*(N-2)
result = ['*'*N+' '*mid+'*'*N]
start = 0
size = N-2
for i in range(2, N+1):
    start, mid = start+1, mid-2
    tmp = ' '*start
    if mid>0: 
        tmp += '*' + ' '*size + '*'
        tmp += ' '*mid
        tmp += '*' + ' '*size + '*'
    else: tmp += '*' + ' '*size + '*' + ' '*size + '*'
    result.append(tmp)
for r in result[:len(result)-1]: print(r)
for r in result[::-1]: print(r)