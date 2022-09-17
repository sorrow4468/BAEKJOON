N, W, H = map(int, input().split())
max_match = W**2 + H**2
result = ['DA', 'NE']
for n in range(N):
    M = int(input())
    if M**2 <= max_match:
        print(result[0])
    else:
        print(result[1])