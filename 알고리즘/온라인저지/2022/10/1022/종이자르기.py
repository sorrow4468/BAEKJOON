import sys

input = sys.stdin.readline

W, H = map(int, input().rstrip().split())
rows, cols = [0, H], [0, W]
N = int(input().rstrip())
for n in range(N):
    D, C = map(int, input().rstrip().split()) # direction, coordinate
    if D: cols.append(C)
    else: rows.append(C)
rows.sort()
cols.sort()
width, height = 0, 0
for i in range(len(rows)-1):
    width = max(width, rows[i+1]-rows[i])
for i in range(len(cols)-1):
    height = max(height, cols[i+1]-cols[i])
print(width*height)