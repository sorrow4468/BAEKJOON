def dfs(size, idx):
    global result

    if arr[2] != 0:
        result += 1
        return

    for player in range(size, N):
        if player not in arr:
            arr[idx] = player
            dfs(player+1, idx+1)
            arr[idx] = 0

N = int(input())
arr = [0]*3
result = 0
dfs(1, 0)
print(result)