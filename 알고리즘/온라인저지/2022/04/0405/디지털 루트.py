def main(n):
    tmp = 0
    for i in str(n):
        tmp += int(i)
    return tmp

while True:
    N = int(input())
    if N == 0:
        break
    result = main(N)
    while len(str(result)) > 1:
        result = main(result)
    print(result)