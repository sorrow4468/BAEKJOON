import sys

input = sys.stdin.readline

for _ in range(int(input().rstrip())):
    A, B = input().rstrip().split()
    A_arr, B_arr = [0]*26, [0]*26
    for a in A: A_arr[ord(a)-97] += 1
    for b in B: B_arr[ord(b)-97] += 1
    result = 'Possible'
    if A_arr != B_arr: result = 'Impossible'
    print(result)