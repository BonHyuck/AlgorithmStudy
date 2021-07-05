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

# 3184. 양
# https://www.acmicpc.net/problem/3184

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def find_area(row, col):
    global sheep, wolf
    # 시작점을 Queue에 넣기
    queue = [(row, col)]
    # 연결된 영역의 양의 수
    S = 0
    # 연결된 영역의 늑대의 수
    W = 0
    # 시작점 확인
    if box[row][col] == "v":
        W += 1
    if box[row][col] == 'o':
        S += 1

    while queue:
        x, y = queue.pop(0)
        # 현재 지점에서 4방향으로 탐색
        for k in range(4):
            new_r = x + dx[k]
            new_c = y + dy[k]
            # 인덱스 확인
            if 0 <= new_r < R and 0 <= new_c < C:
                # 방문처리가 안됐으며, 울타리가 아닌곳
                if visited[new_r][new_c] == 0 and box[new_r][new_c] != "#":
                    # 방문처리 해주기
                    visited[new_r][new_c] = 1
                    # 다음에 검사해야하므로 Queue에 넣어두기
                    queue.append((new_r, new_c))
                    # 늑대 확인
                    if box[new_r][new_c] == "v":
                        W += 1
                    # 양 확인
                    elif box[new_r][new_c] == 'o':
                        S += 1
    # 영역 검사 완료
    # 양이 더 많으면
    if S > W:
        # 늑대는 없어지고 양의 개수만 더하기
        sheep += S
    # 늑대가 더 많거나 수가 같으면?
    else:
        # 양이 없어지고 늑대의 개수만 더하기
        wolf += W
    # 함수 끝
    return


R, C = map(int, input().split())
box = [list(input()) for _ in range(R)]
# 방문처리
visited = [[0 for _ in range(C)] for _ in range(R)]
# 양의 수
sheep = 0
# 늑대의 수
wolf = 0
# 전체 배열을 돌기
for r in range(R):
    for c in range(C):
        # 아직 방문을 안했으며 울타리가 아닌곳부터 시작
        if visited[r][c] == 0 and box[r][c] != "#":
            # 방문처리
            visited[r][c] = 1
            find_area(r, c)

print(sheep, wolf)