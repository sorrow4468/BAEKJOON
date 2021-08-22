N = int(input())
str_numbers = input()
numbers = []
for number in str_numbers:
    numbers.append(int(number))
print(sum(numbers))