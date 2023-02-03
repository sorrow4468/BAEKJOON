input()
result = 1
words = input().split()
palindrome = words[0][0]
for word in words:
    if word[0] != palindrome or word[-1] != palindrome: 
        result = 0
        break
print(result)