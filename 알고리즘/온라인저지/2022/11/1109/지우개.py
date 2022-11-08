import sys

input = sys.stdin.readline

N = int(input().rstrip())
arr = list(range(1, N+1))
while len(arr) > 1:
    pop_idx_list = []
    for i in range(len(arr)):
        if not i%2:
            pop_idx_list.append(i)
    for pop_idx in pop_idx_list[::-1]:
        arr.pop(pop_idx)
print(arr[0])