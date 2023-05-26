for i in range(1, int(input())+1):
    result = ''
    if not i%7 and i%11:
        result = 'Hurra!'
    if i%7 and not i%11:
        result = 'Super!'
    if not i%7 and not i%11:
        result = 'Wiwat!'
    print(result if result else i)