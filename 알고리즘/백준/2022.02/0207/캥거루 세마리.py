A, B, C = map(int, input().split())

further = A

if (B-A) < (C-B):
    further = C

print(abs(further - B) - 1)
