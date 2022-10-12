for _ in range(int(input())):
    inputs = list(map(int, input().split()))
    stats = []
    stats.append(max(1, inputs[0]+inputs[4]))
    stats.append(max(1, inputs[1]+inputs[5]))
    stats.append(max(0, inputs[2]+inputs[6]))
    stats.append(inputs[3]+inputs[7])
    print(stats[0] + stats[1]*5 + stats[2]*2 + stats[3]*2)