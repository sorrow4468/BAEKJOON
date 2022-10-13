import sys

input = sys.stdin.readline

i = 0
while True:
    i += 1
    N = int(input())
    if N == 0: break
    result = [N]
    result.append(3*result[0])
    if not result[1]%2: result.append(result[1]//2)
    else: result.append((result[1]+1)//2)
    result.append(3*result[2])
    result.append(result[3]//9)
    odd_or_even = ['even', 'odd']
    print('{}. {} {}'.format(i, odd_or_even[result[1]%2], result[4]))