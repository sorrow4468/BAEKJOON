S = input()
result = set()
for i in range(1, len(S)+1):
    # print(i)
    for j in range(len(S)+1-i):
        # print(j, j+i)
        # print(S[j:j+i])
        result.add(S[j:j+i])
print(len(result))