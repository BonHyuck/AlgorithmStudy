#
# monkey_r = [-1, 1, 0, 0]
# monkey_c = [0, 0, -1, 1]
# horse_r = [-1, -2, -2, -1, 1, 2, 2, 1]
# horse_c = [-2, -1, 1, 2, 2, 1, -1, -2]
#
# K = int(input())
# N, M = map(int, input().split())
# box = [list(map(int, input().split())) for _ in range(N)]
# visited = [[float('inf') for _ in range(M)] for _ in range(N)]
# queue = [[(0, 0, 0)]]
# visited[0][0] = 1
# cnt = 1
# while queue:
#     points = queue.pop(0)
#     next_points = []
#     for row, col, horse in points:
#         # 말처럼 무빙 가능
#         if horse < K:
#             for h in range(8):
#                 new_r = row + horse_r[h]
#                 new_c = col + horse_c[h]
#                 # 인덱스 확인
#                 if 0 <= new_r < N and 0 <= new_c < M:
#                     if visited[new_r][new_c] >= cnt and box[new_r][new_c] == 0:
#                         visited[new_r][new_c] = cnt
#                         next_points.append((new_r, new_c, horse + 1))
#         # 원숭이 무빙
#         for k in range(4):
#             new_r = row + monkey_r[k]
#             new_c = col + monkey_c[k]
#             # 인덱스 확인
#             if 0 <= new_r < N and 0 <= new_c < M:
#                 if visited[new_r][new_c] >= cnt and box[new_r][new_c] == 0:
#                     visited[new_r][new_c] = cnt
#                     next_points.append((new_r, new_c, horse))
#     cnt += 1
#     if len(next_points) > 0:
#         queue.append(next_points)
#     else:
#         break
# # print(visited)
# if visited[N-1][M-1] != float('inf'):
#     print(visited[N-1][M-1])
# else:
#     print(-1)

monkey_r = [-1, 1, 0, 0]
monkey_c = [0, 0, -1, 1]
horse_r = [-1, -2, -2, -1, 1, 2, 2, 1]
horse_c = [-2, -1, 1, 2, 2, 1, -1, -2]

K = int(input())
N, M = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visited = [[float('inf') for _ in range(M)] for _ in range(N)]
visited[0][0] = 1
queue = [(0, 0, 0, 0)]
result = -1
while queue:
    row, col, cnt, horse = queue.pop(0)
    if row == N - 1 and col == M - 1:
        result = cnt
        break
    if horse < K:
        for h in range(8):
            new_r = row + horse_r[h]
            new_c = col + horse_c[h]
            if 0 <= new_r < N and 0 <= new_c < M:
                if box[new_r][new_c] == 0 and visited[new_r][new_c] >= cnt + 1:
                    visited[new_r][new_c] = cnt + 1
                    queue.append((new_r, new_c, cnt + 1, horse + 1))
    for k in range(4):
        new_r = row + monkey_r[k]
        new_c = col + monkey_c[k]
        if 0 <= new_r < N and 0 <= new_c < M:
            if box[new_r][new_c] == 0 and visited[new_r][new_c] >= cnt + 1:
                visited[new_r][new_c] = cnt + 1
                queue.append((new_r, new_c, cnt + 1, horse))

# print(visited)
print(result)
