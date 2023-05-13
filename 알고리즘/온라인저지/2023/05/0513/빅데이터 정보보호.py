input()
S = input()
bigdata, security = S.count('b'), S.count('s')
result = 'bigdata? security!'
if bigdata > security:
    result = 'bigdata?'
if bigdata < security:
    result = 'security!'
print(result)