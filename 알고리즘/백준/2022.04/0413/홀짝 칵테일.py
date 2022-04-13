from itertools import combinations

nums = list(map(int, input().split()))
nums.sort(reverse=True)
odd_drinks = []
even_drinks = []
for i in range(1, len(nums)+1):
    tmp = list(combinations(nums, i))
    # print(tmp)
    for t in tmp:
        a = 1
        for j in t:
            # print(j)
            a *= j
        if a%2:
            odd_drinks.append(a)
        else:
            even_drinks.append(a)
odd_drinks.sort(reverse=True)
even_drinks.sort(reverse=True)
if odd_drinks:
    print(odd_drinks[0])
else:
    print(even_drinks[0])