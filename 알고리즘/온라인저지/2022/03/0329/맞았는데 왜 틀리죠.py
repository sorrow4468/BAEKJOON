S1, S2 = map(int, input().split())
result = 'Accepted'
is_wrong_answer = False
is_why_wrong = False
for s in range(S1):
    A, B = map(int, input().split())
    if A != B:
        is_wrong_answer = True
for s in range(S2):
    A, B = map(int, input().split())
    if A != B:
        is_why_wrong = True
if is_wrong_answer:
    result = 'Wrong Answer'
elif is_why_wrong:
    result = 'Why Wrong!!!'
print(result)
