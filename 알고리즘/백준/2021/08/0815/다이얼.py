dial = {2:"ABC", 3:"DEF", 4:"GHI", 5:"JKL", 6:"MNO", 7:"PQRS", 8:"TUV", 9:"WXYZ"}
word = input()
result = 0
for wor in word:
    for dil in dial:
        if wor in dial[dil]:
            result += dil
result += len(word)
print(result)