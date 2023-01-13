while True:
    tmp = input()
    if tmp == '#': break
    result = set()
    for t in tmp.lower():
        if 97<=ord(t)<97+26:
            result.add(t)
    print(len(result))