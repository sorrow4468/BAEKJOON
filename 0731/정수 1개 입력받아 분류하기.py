a = int(input())
def odd_even(n): # True: 홀수, False: 짝수
    if n % 2 == True:
        return True
    else:
        return False

def plus_minus(n): # True: 양수, False: 짝수
    if n >= 0:
        return True
    else:
        return False

if odd_even(a) == False and plus_minus(a) == False:
    print("A") # A: - and even
elif plus_minus(a) == False and odd_even(a) == True:
    print("B") # B: - and odd
elif plus_minus(a) == True and odd_even(a) == False:
    print("C") # C: + and even
else:
    print("D") # D: + and odd