def dfs(w, h, depth, tmp):
    global visited, maxx
    print(h, w, depth, tmp)
    # print(visited)
    if depth == 4:
        # print('depth 4 here', w, h, depth, tmp)
        if tmp > maxx:
            maxx = tmp
            print('THIS IS MAXX😊😉😊😊', maxx)
        return
    for i in range(6):
        if (0 <= w+dx[i] < W) and (0 <= h+dy[i] < H) and not visited[h+dy[i]][w+dx[i]]:
            visited[h+dy[i]][w+dx[i]] = 1
            dfs(w+dx[i], h+dy[i], depth+1, tmp+arr[h+dy[i]][w+dx[i]])
            visited[h+dy[i]][w+dx[i]] = 0

# 12시 방향부터 시계방향으로 델타이동
dx = [0, 1, 1, 0, -1, -1]
dy = [-1, -1, 0, 1, 0, -1]
T = int(input())
for t in range(1, T+1):
    W, H = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(H)]
    # print(arr)
    maxx = 0
    for h in range(H):
        for w in range(W):
            visited = [[0]*W for _ in range(H)]
            visited[h][w] = 1
            dfs(w, h, 1, arr[h][w])
            print('------------------')
    print(maxx ** 2)


# def dfs(i, depth, tmp):
#     global visited, maxx
#     print(i, depth, tmp)
#     if depth == 4:
#         # print('depth 4 here', w, h, depth, tmp)
#         if tmp > maxx:
#             maxx = tmp
#             print('THIS IS MAXX😊😉😊😊', maxx)
#         return
#     for j in range(6):
#         if (1 <= i+dx[j] < W*H+1) and not visited[i+dx[j]]:
#             visited[i+dx[j]] = 1
#             dfs(i+dx[j], depth+1, tmp+arr[i+dx[j]])
#             visited[i+dx[j]] = 0

# dx = [-5, -4, 1, 5, -1, -6]
# T = int(input())
# for t in range(1, T+1):
#     W, H = map(int, input().split())
#     arr = [0]
#     for h in range(H):
#         arr += list(map(int, input().split()))
#     maxx = 0
#     for i in range(1, W*H+1):
#         visited = [0] * len(arr)
#         visited[i] = 1
#         dfs(i, 1, arr[i])
#         print('------------------')
#     print(maxx ** 2)
# print(arr[9])    