sen = input()

i = 10

lenn = len(sen)

while i < lenn:
    print(sen[i-10:i])
    i += 10

print(sen[i-10:lenn])
