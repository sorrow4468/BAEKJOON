result = ['even', 'odd']
for _ in range(int(input())):
    X = int(input())
    print(f'{X} is {result[X%2]}')