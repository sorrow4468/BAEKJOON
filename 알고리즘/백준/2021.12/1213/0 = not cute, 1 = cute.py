T = int(input())

cute = 0
cut = 0

for tc in range(T):
    is_cute = int(input())

    if is_cute:
        cute += 1
    else:
        cut += 1

if cute < cut:
    print('Junhee is not cute!')
else:
    print('Junhee is cute!')