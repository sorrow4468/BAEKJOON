T = int(input())
for t in range(T):
    result = 'NOT '
    arr = input().split()
    word1 = [0] * 26
    word2 = [0] * 26
    for w in arr[0]:
        word1[ord(w)-97] += 1
    for w in arr[1]:
        word2[ord(w)-97] += 1
    if word1 == word2:
        result = ''
    print('{} & {} are {}anagrams.'.format(
        arr[0], arr[1], result
    ))
