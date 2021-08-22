x, y, w, h = map(int, input().split())
distance = []
distance.append(min(x, w-x))
distance.append(min(y, h-y))
print(min(distance))