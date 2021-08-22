T = int(input())
numbers = []
for tc in range(T):
    numbers.append(int(input()))
numbers.sort()
for number in numbers:
    print(number)