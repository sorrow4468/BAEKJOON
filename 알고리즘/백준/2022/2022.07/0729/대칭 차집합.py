A, B = map(int, input().split())
A_list = list(map(int, input().split()))
A_set = set(A_list)
B_list = list(map(int, input().split()))
B_set = set(B_list)
result = []
for a in A_list:
    if a not in B_set:
        result.append(a)
for b in B_list:
    if b not in A_set:
        result.append(b)
print(len(result))