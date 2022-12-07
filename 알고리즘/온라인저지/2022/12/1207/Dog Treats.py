result = 0
for i in range(1, 4):
    result += int(input())*i
print('happy' if result >= 10 else 'sad')