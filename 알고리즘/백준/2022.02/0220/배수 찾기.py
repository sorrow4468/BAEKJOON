N = int(input())

while True:
    num = int(input())
    if not num:
        break

    print(f'{num} is a multiple of {N}.' if not num%N else f'{num} is NOT a multiple of {N}.')