data = {
    "TV": 2000000,
    "냉장고": 1500000,
    "책상": 350000,
    "노트북": 1200000,
    "가스레인지": 200000,
    "세탁기": 1000000,
}

tmp = []

for d in data:
    tmp.append((d, data[d]))

tmp.sort(key=lambda x: x[1], reverse=True)

for t in tmp:
    print('{}: {}'.format(t[0], t[1]))

