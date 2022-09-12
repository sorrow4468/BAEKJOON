n = int(input())

# result = 0
# dim = 3

# for i in range(1, n-1):
#     for j in range(i+1, n):
#         for k in range(j+1, n+1):  
#             result += 1
#             print(i, j, k)

result = 0
dim = 3

for i in range(1, n-1):
    # result += sum(list(range(1, i+1)))
    result += i * (n-i-1)

print(result, f'\n{dim}', sep='')