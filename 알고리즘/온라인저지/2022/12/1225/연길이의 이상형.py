yeongil = input()
dictt = {
    'E': 'I', 'I':'E',
    'S': 'N', 'N':'S',
    'T': 'F', 'F':'T',
    'J': 'P', 'P':'J',
}
for y in yeongil:
    print(dictt[y], end='')