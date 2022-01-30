grade = input()

alpha = {
    'A': 4,
    'B': 3,
    'C': 2,
    'D': 1,
    'F': 0,
    '+': 0.3,
    '0': 0.0,
    '-': -0.3,
},

result = 0



for g in grade:
    result += alpha[0][g]
    

print('{:.1f}'.format(result))