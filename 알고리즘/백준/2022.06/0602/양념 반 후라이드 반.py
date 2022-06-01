A, B, C, X, Y = map(int, input().split())
x = min(X, Y)
y = max(X, Y)
result = 0
if C > (A+B)//2:
    result += A*X + B*Y
else:
    result += C*x*2
    if X != Y:
        if X > Y:
            result += A*(y-x)
        else:
            result += B*(y-x)
    tmp = C*y*2
    if result > tmp:
        result = tmp
print(result)