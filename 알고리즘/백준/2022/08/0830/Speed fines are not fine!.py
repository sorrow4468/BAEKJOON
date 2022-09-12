F = [100, 270, 500] # fine
A = int(input())
B = int(input())
i = 0
if B > A:
    if 21<=B-A<=30: i = 1
    elif 31<=B-A: i = 2
print(f'You are speeding and your fine is ${F[i]}.' if B > A else 'Congratulations, you are within the speed limit!')