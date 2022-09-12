S = input()
alphabet = [chr(i+97) for i in range(26)]
# print(alphabet)
result = 0
word = ''
s = 0 # S index
while True:
    result += 1
    for a in alphabet:
        if a == S[s]:
            word += a
            if word == S:
                print(result)
                exit()
            s += 1
            # print(result, word, s)