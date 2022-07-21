B, C, D = map(int, input().split())
burger = list(map(int, input().split()))
side = list(map(int, input().split()))
drink = list(map(int, input().split()))
burger.sort(reverse=True)
side.sort(reverse=True)
drink.sort(reverse=True)
min_set = min(len(burger), len(side), len(drink))
result1 = sum(burger) + sum(side) + sum(drink)
print(result1)
result2 = result1
for i in range(min_set):
    result2 -= burger[i] * 0.1
    result2 -= side[i] * 0.1
    result2 -= drink[i] * 0.1
print(f'{result2:.0f}')