# dx = [-1, 1, 0, 0]
# dy = [0, 0, -1, 1]
#
# def find_area(row, col):
#     global sheep, wolf
#
#     # 방문 처리
#     visited[row][col] = 1
#     # 양인가?
#     if box[row][col] == "o":
#         sheep += 1
#     # 늑대인가?
#     if box[row][col] == "v":
#         wolf += 1
#
#     for k in range(4):
#         new_r = row + dx[k]
#         new_c = col + dy[k]
#         if 0 <= new_r < R and 0 <= new_c < C:
#             if visited[new_r][new_c] == 0 and box[new_r][new_c] != "#":
#                 find_area(new_r, new_c)
#
#     return
#
# R, C = map(int, input().split())
# box = [list(input()) for _ in range(R)]
# visited = [[0 for _ in range(C)] for _ in range(R)]
# sheep_wolf = []
# sheep = 0
# wolf = 0
# for r in range(R):
#     for c in range(C):
#         if visited[r][c] == 0 and box[r][c] != "#":
#             find_area(r, c)
#             sheep_wolf.append((sheep, wolf))
#             sheep = 0
#             wolf = 0
#
# sheep_result = 0
# wolf_result = 0
#
# for s, w in sheep_wolf:
#     if s > w:
#         sheep_result += s
#     elif s <= w:
#         wolf_result += w
#
# print(sheep_result, wolf_result)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_area(row, col):
    global sheep, wolf
    queue = [(row, col)]
    S = 0
    W = 0
    if box[row][col] == "v":
        W += 1
    if box[row][col] == 'o':
        S += 1

    while queue:
        x, y = queue.pop(0)
        for k in range(4):
            new_r = x + dx[k]
            new_c = y + dy[k]
            if 0 <= new_r < R and 0 <= new_c < C:
                if visited[new_r][new_c] == 0 and box[new_r][new_c] != "#":
                    visited[new_r][new_c] = 1
                    queue.append((new_r, new_c))
                    if box[new_r][new_c] == "v":
                        W += 1
                    elif box[new_r][new_c] == 'o':
                        S += 1
    if S > W:
        sheep += S
    else:
        wolf += W
    return


R, C = map(int, input().split())
box = [list(input()) for _ in range(R)]
visited = [[0 for _ in range(C)] for _ in range(R)]
sheep = 0
wolf = 0
for r in range(R):
    for c in range(C):
        if visited[r][c] == 0 and box[r][c] != "#":
            visited[r][c] = 1
            find_area(r, c)

print(sheep, wolf)