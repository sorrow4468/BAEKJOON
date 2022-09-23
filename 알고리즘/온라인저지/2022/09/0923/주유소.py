import sys

input = sys.stdin.readline

N = int(input().rstrip())
distances = list(map(int, input().rstrip().split()))
fuels = list(map(int, input().rstrip().split()))
refuel = []
fuel_min = int(1e9)
for i in range(len(fuels)-1):
    if fuels[i] < fuel_min:
        refuel.append(i)
        fuel_min = min(fuel_min, fuels[i])
refuel.append(len(fuels)-1)
result = 0
for i in range(len(refuel)-1):
    result += sum(distances[refuel[i]:refuel[i+1]])*fuels[refuel[i]]
print(result)

# https://www.acmicpc.net/problem/13305