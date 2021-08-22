
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)

print(factorial(10))

"""
재귀함수
def 재귀():
    if 기저:
        return 
    else: 기저 아닐 때
        return 
"""