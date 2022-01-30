url = 'http://www.example.com/test?p=1&q=2'

protocol = ''
host = ''
others = ''

host_s = 0
host_e = 0

for i in range(len(url)):
    if url[i] == ':':
        protocol = url[:i]
    
    if url[i:i+3] == 'www':
        host_s = i
    
    if url[i-2:i+1] == 'com':
        host_e = i+1

        others = url[host_e+1:]

host = url[host_s:host_e]

print('protocol: {}'.format(protocol))
print('host: {}'.format(host))
print('others: {}'.format(others))