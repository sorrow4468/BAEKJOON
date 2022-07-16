fees = list(map(int, input().split()))
result = 0
parking = [0] * 101
for i in range(3):
    IN, OUT = map(int, input().split())
    for j in range(IN, OUT):
        parking[j] += 1
for p in parking:
    result += p*fees[p-1]
print(result)

"""
1 2 3 4 5 
    3 4 
  2 3 4 5 6 7 
5 6 3 3 6 5 5
17      20    36
"""
# print(sum([5, 6, 6, 6, 5, 5]))