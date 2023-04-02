N, H, V = map(int, input().split())
print(max(N-H, H)*max(N-V, V)*4)