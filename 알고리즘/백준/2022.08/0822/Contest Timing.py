D, H, M = map(int, input().split())
result = (D-11)*24*60 + (H-11)*60 + (M-11)
print(result if result >= 0 else -1)