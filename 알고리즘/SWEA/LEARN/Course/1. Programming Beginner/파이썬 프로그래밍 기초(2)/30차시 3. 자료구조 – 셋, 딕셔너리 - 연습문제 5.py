fruit = ['   apple    ','banana','  melon']

result = {}

for f in fruit:
    f = f.lstrip()
    f = f.rstrip()
    result.update({f:len(f)})

print(result)

