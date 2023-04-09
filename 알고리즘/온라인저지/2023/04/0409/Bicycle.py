nums = [int(input()) for _ in range(5)]
a, x, b, y, T = nums
result = [a, b]
A = max(0, T-30)
B = max(0, T-45)
result[0] += A*x*21
result[1] += B*y*21
print(*result)