A, B, C = map(int, input().split())
result = 'N'
if A == B: 
    result = 'S'
if C == B: 
    result = 'S'
if A == C: 
    result = 'S'
if A+C == B: 
    result = 'S'
if A == B+C: 
    result = 'S'
if A+B == C: 
    result = 'S'
print(result)